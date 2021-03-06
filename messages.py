account = dict(
    welcome='\n\nSeems like its your first time logging in to this seed!\n'
            'By default the wallet will connect'
            ' to testnet node http://bahamapascal-tn1.ddns.net:14200'
            '(while in Beta)\n'
            'Do you want to connect to another host?\n\n',
    login_welcome='\n\n\n------------------------------------------------'
        'Account login---------------------------------------'
        '-----------------'
        '\n\nA seed should only contain the letters A-Z and 9.'
        ' Lowercase letters will automatically be converted to\n'
        'uppercase and everything else that is not A-Z,'
        ' will be converted to a 9.',
    enter_seed='\n \nPlease enter your'
                            ' seed to login to your account: ',
    seed_hash='\n\nThe Sha256 hash of your seed is',
    seed_review='Should the seed be displayed for review?\n',
    entered_seed='You entered {} as seed.',
    seed_display_prompt='OK, seed won\'t be displayed!',
    choose_host='\nPlease enter the host you want to connect to: ',
    new_host_set='New host set to {} ',
    keeping_default_host='All right! I would not change the default host'
)

account_info = dict(
    scan_balance_prompt='\n\nThis seems to be the first time '
                        'you are using this account with the CL wallet!\n'
                        'If you are expecting balance on this account'
                        ' you should scan for balance.\n'
                        'Do you want to scan for balance?\n\n ',
    address_generation_prompt='\n\nOkay great, I will generate addresses'
                        ' and check them for balance!\n'
                        'Please tell me how many addresses'
                        ' I should check. If you say 100\n'
                        'I will generate addresses until balance'
                        ' is found or until 100 addresses\n'
                        'have been generated.\n'
                        'So, whats the maximum number of '
                        'addresses I should check?\n\n',
    maximum_addresses_prompt='Please enter the max number of addresses to check: ',
    no_addresses_entered='You entered 0! I won\'t check any addresses.',
    generate_deposit_address='\nOkay, then I will just generate a deposit address.\n'
                             'In case you wan\'t to generate addresses'
                             ' after that, you can use the \'find balance\' command.\n'
                             'Generating deposit address...\n\n\n',
    address_balance_info='Index: {} ' \
                           + ' Address  ' + '{}' \
                           + '   balance: ' \
                           + '{}' \
                           + '\n',
    invalid_checksum='Index: {} ' \
                      + '   Invalid Checksum!!!' \
                      + '\n',
    deposit_address='\n' + 'Deposit address: ',
    total_balance='\nTotal Balance: ',
    first_index_with_balance='First index with balance {}',
    last_index_with_balance='Last index with balance {}',
    no_data='No data to display.'
)

account_history = dict(
    new_transactions='\n\n\nNew transactions.',
    old_transactions='\n\n\nOld transactions.',
    full_transactions_history='\n\n\nFull transactions.',
    transactions_to_from='\nTransactions to/from {}',
    no_transactions_history='No transactions in history'
)

address_manager=dict(
    invalid_checksum='Invalid checksum!!!',
    generating_address='Generating address...',
    deposit_address_exception='An error occurred while trying to get the deposit address'
)

balance = dict(
    generating_addresses='Generating addresses'
                         ' and checking for balance, please wait...\n',
    checking_addresses='Checking address {} in range of {}',
    balance_found='Balance found. \n\nIndex: {} \n\n Address: {} \n\n Balance: {}',
    no_address_with_balance='No address with balance found.',
    start_index_not_found='Start index was not found. You should generate more addresses or use a lower start index'
)

wallet = dict(
    welcome='\nStarting wallet...\n\n\n\n'
)

helpers = dict(
    balance_finder_general='How many addresses should be checked? ',
    balance_finder_address_number_prompt='How many address should I generate? ',
    invalid_number='You did not enter a number.'
)

settings = dict(
    description_min_weight_magnitude='Enter "min_weight_magnitude" to set the minWeightMagnitude',
    description_units='Enter "unit" to set the Units used to display iota tokens (i,Ki,Mi,Gi,Ti)',
    description_host='Enter "host" to set a new host to connect to',
    description_current_settings='Enter "current_settings" to see',
    description_back='Enter "back" to quit the settings menu\n\n',
    command_input='Please enter a command: ',
    enter_min_weight_magnitude='\nPlease enter the minWeightMagnitude: ',
    min_weight_magnitude_set='minWeightMagnitude set to {} \n\n',
    enter_units='\nPlease enter "i","ki","mi","gi" or "ti": ',
    units_set='Units set to ' + "{}" + '\n\n',
    invalid_unit='\n\nOops! Looks like you entered something else than "i","ki","mi","gi" or "ti"',
    enter_host='\nPlease enter the host you want to connect to: ',
    host_set='Host set to {} \n\n',
    currently_set=dict(
        mwm='Minimum Weight Magnitude',
        host='Host',
        units='Units'
    )
)

common = dict(
    try_again='Please try again.',
    invalid_command='Looks like you entered an incorrect command.'
)

help = dict(
    account_info=dict(
        command='account info',
        description='Will show you each address containing balance, total balance and your deposit address.'
    ),
    full_account_info=dict(
        command='full account info',
        description='Will show you all saved addresses and there corresponding balance.'
    ),
    find_balance=dict(
        command='find balance',
        description='Searches for the first address with balance within a user defined range(e.g. first 100 addresses)'
    ),
    generate_new_address=dict(
        command='generate new address',
        description='Generates one new addresses.'
    ),
    send_transfer=dict(
        command='send transfer',
        description='Allows you to make one or more transfers.'
    ),
    account_history=dict(
        command='account history',
        description='Shows all confirmed transfers and all new transfers (from your saved account addresses)'
    ),
    full_account_history=dict(
        command='full account history',
        description='Shows all transfers, including old non confirmed transfers (from your saved account addresses).'
    ),
    replay_bundle=dict(
        command='replay <short-transaction-id>',
        description='Re-attach transactions to a different part of the Tangle.'
    ),
    settings=dict(
        command='settings',
        description='Set the minWeightMagnitude and the Units used to display iota tokens (i,Ki,Mi,Gi,Ti)'
    ),
    log_out=dict(
        command='logout',
        description='Log out of your account and login with a different seed'
    ),
    exit=dict(
        command='exit',
        description='Exit the wallet.'
    )
)

manage=dict(
    help_info='\n \nPlease enter a command. \n\nType help to see all available commands: ',
    invariant='Looks like you entered a wrong command.',
    generate_new_address='Generating a new address...'
)

transfer = dict(
    receiving_address_prompt='\nPlease enter receiving address: ',
    address_without_checksum_warning='You entered an address without checksum. Are you sure you want to continue?',
    address_with_checksum='Good choice. Addresses with checksum are a lot safer to use.',
    invalid_address='Invalid address.',
    valid_address_info='Address must be 81 or 90 characters long.',
    number_and_unit_promot='''
    Enter a number and the the unit size.
    Available units are "i" Iota, "ki" (Kilo Iota), "mi" (Mega Iota), "gi" (Giga Iota), "ti" (Terra Iota).
    
    Example: 12.3 gi
    
    ''',
    amount_to_send_prompt='Please enter amount to send: ',
    invalid_amount='You entered an amount greater than zero but smaller than 1 IOTA. Can only send whole IOTAs.',
    insufficient_balance='You do not have sufficient balance. The available balance is {}',
    invalid_unit_size='You did not enter a valid unit size.',
    invalid_value='You did not enter a valid value.',
    enter_message_prompt='Please enter a message: ',
    enter_tag_prompt='Please enter a tag: ',
    additional_transfer='Do you want to prepare another transfer?',
    sending_transfer='Sending transfer... This may take a while.',
    completed='Transaction completed.'
)
