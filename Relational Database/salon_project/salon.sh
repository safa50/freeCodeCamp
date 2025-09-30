#! /bin/bash

# PSQL variable for easy querying.
# -t (tuples only), --no-align (no padding), -c (command)
PSQL="psql --username=freecodecamp --dbname=salon -t --no-align -c"

echo -e "\n~~~~~ MY SALON ~~~~~\n"
echo "Welcome to My Salon, how can I help you?"

MAIN_MENU() {
  # Display error message if passed one
  if [[ $1 ]]
  then
    echo -e "\n$1"
  fi

  # Get and display numbered list of services
  SERVICES_LIST=$($PSQL "SELECT service_id, name FROM services ORDER BY service_id")
  echo "$SERVICES_LIST" | while IFS="|" read SERVICE_ID NAME
  do
    echo "$SERVICE_ID) $NAME"
  done

  # Add the Exit option
  echo "0) Exit"

  # Prompt for service selection
  read SERVICE_ID_SELECTED

  # check if service exists and get its name (only if it is not 0)
  if [[ ! $SERVICE_ID_SELECTED =~ ^[0-9]+$ ]]
  then
    MAIN_MENU "Please enter a valid number from the list. What would you like today?"
    return
  else
    if [[ $SERVICE_ID_SELECTED != 0 ]]
    then
      SERVICE_NAME=$($PSQL "SELECT name FROM services WHERE service_id = $SERVICE_ID_SELECTED")
    fi
  fi
  
  case $SERVICE_ID_SELECTED in
    # 0 is the Exit option
    0) 
      EXIT 
      return
      ;;

    # Any other input
    *) 
      # if the query returned an empty string, the ID was invalid.
      if [[ -z $SERVICE_NAME ]]
      then
        MAIN_MENU "I could not find that service. What would you like today?"
      else
        # Valid service selected, proceed to book appointment
        APPOINTMENT_MENU
      fi
      ;;
  esac
}

APPOINTMENT_MENU () {
  # The SERVICE_NAME and SERVICE_ID_SELECTION are already  set from the MAIN MENU

  # GET customer phone number
  echo -e "\nWhat's your phone number?"
  read CUSTOMER_PHONE

  # Check if exists and get their ID
  CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone = '$CUSTOMER_PHONE'")

  # If customer doesn't exist
  if [[ -z $CUSTOMER_ID ]]
  then
    # GET new customer name
    echo -e "\nI don't have a record for that phone number, what's your name?"
    read CUSTOMER_NAME

    # INSERT new customer
    INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(phone, name) VALUES ('$CUSTOMER_PHONE', '$CUSTOMER_NAME')")

    # GET new customer ID
    CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone = '$CUSTOMER_PHONE'")
  else
    # GET existing customer name
    CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE customer_id = '$CUSTOMER_ID'")
  fi

  # Get appointment time
  echo -e "\nWhat time would you like your $SERVICE_NAME, $CUSTOMER_NAME?"
  read SERVICE_TIME

  # Insert new appointment
  INSERT_APPOINTMENT_RESULT=$($PSQL "INSERT INTO appointments(customer_id, service_id, time) VALUES($CUSTOMER_ID, $SERVICE_ID_SELECTED, '$SERVICE_TIME')")

  # Final confirmation message
  echo -e "\nI have put you down for a $SERVICE_NAME at $SERVICE_TIME, $CUSTOMER_NAME."
}

EXIT() {
    echo -e "\nThank you for stopping by!\n"
}

# Start the application
MAIN_MENU