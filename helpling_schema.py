import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay

helpling_schema = sgqlc.types.Schema()

# Unexport Node/PageInfo, let schema re-declare them
helpling_schema -= sgqlc.types.relay.Node
helpling_schema -= sgqlc.types.relay.PageInfo


########################################################################
# Scalars and Enumerations
########################################################################
class AbTestGroupType(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('control', 'experiment', 'experiment2')


class BidStateEnumType(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('REQUEST', 'CONFIRMED', 'PAYMENT', 'UNCONFIRMED', 'UNSUCCESSFUL', 'INCOMPLETE', 'CANCELLED')


Boolean = sgqlc.types.Boolean


class BusySlotType(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('BUSY', 'AVAILABLE', 'CURRENT')


class ConfirmProviderFirstEventEnum(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('accept', 'reject')


class CustomerBidPotentialCandidateOrderFields(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('priceAsc', 'priceDesc', 'jobsDoneAsc', 'jobsDoneDesc', 'relevance')


class CustomerCommitmentEnum(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('no_commitment', 'three_months', 'six_months', 'twelve_months')


class CustomersFilterEnumType(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('current', 'old', 'one_off', 'recurring')


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime


class EventFeeling(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('POSITIVE', 'NEGATIVE', 'NEUTRAL', 'NONE')


class ExperienceTypeExperienceTimeKeyEnum(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = (
    'not_applicable', 'experience_none', 'experience_1_6_months', 'experience_6_12_months', 'experience_1_3_years',
    'experience_more_than_3_years')


Float = sgqlc.types.Float


class Frequency(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('once', 'week', 'fortnight', 'repeat')


ID = sgqlc.types.ID

Int = sgqlc.types.Int


class MessageKind(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('READ', 'UNREAD', 'ALL')


class Money(sgqlc.types.Scalar):
    __schema__ = helpling_schema


class MoneyFormat(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('WithCurrency', 'Plain', 'Integer')


class OnboardingRequirementStatusEnum(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('incomplete', 'in_progress', 'complete')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('ASC', 'DESC')


class PromoValueType(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('ABSOLUTE', 'PERCENTAGE', 'HOURLY')


String = sgqlc.types.String


class TimeUnit(sgqlc.types.Enum):
    __schema__ = helpling_schema
    __choices__ = ('SECONDS', 'HOURS')


class Upload(sgqlc.types.Scalar):
    __schema__ = helpling_schema


########################################################################
# Input Objects
########################################################################
class AreaType(sgqlc.types.Input):
    __schema__ = helpling_schema
    postcode = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='postcode')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')


class HelpCenterTestItemsType(sgqlc.types.Input):
    __schema__ = helpling_schema
    tools_blog = sgqlc.types.Field(Boolean, graphql_name='tools_blog')
    tools_email = sgqlc.types.Field(Boolean, graphql_name='tools_email')
    tools_faq = sgqlc.types.Field(Boolean, graphql_name='tools_faq')
    tools_online_articles = sgqlc.types.Field(Boolean, graphql_name='tools_online_articles')
    tools_other = sgqlc.types.Field(String, graphql_name='tools_other')
    tools_printable_articles = sgqlc.types.Field(Boolean, graphql_name='tools_printable_articles')
    tools_tutorials = sgqlc.types.Field(Boolean, graphql_name='tools_tutorials')
    tools_video = sgqlc.types.Field(Boolean, graphql_name='tools_video')
    topics_managing_bookings = sgqlc.types.Field(Boolean, graphql_name='topics_managing_bookings')
    topics_managing_calendar = sgqlc.types.Field(Boolean, graphql_name='topics_managing_calendar')
    topics_managing_price = sgqlc.types.Field(Boolean, graphql_name='topics_managing_price')
    topics_managing_ratings = sgqlc.types.Field(Boolean, graphql_name='topics_managing_ratings')
    topics_managing_relationships = sgqlc.types.Field(Boolean, graphql_name='topics_managing_relationships')
    topics_optimizing_profile = sgqlc.types.Field(Boolean, graphql_name='topics_optimizing_profile')
    topics_other = sgqlc.types.Field(String, graphql_name='topics_other')
    topics_quality_of_clean = sgqlc.types.Field(Boolean, graphql_name='topics_quality_of_clean')
    topics_receiving_offers = sgqlc.types.Field(Boolean, graphql_name='topics_receiving_offers')


class PostedMessage(sgqlc.types.Input):
    __schema__ = helpling_schema
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    provider_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='providerId')


class ReviewMessage(sgqlc.types.Input):
    __schema__ = helpling_schema
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    relationship_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='relationshipId')


class UserBookingDetailsInput(sgqlc.types.Input):
    __schema__ = helpling_schema
    instabook_enabled = sgqlc.types.Field(Boolean, graphql_name='instabookEnabled')


class UserProfileAbilityInput(sgqlc.types.Input):
    __schema__ = helpling_schema
    pets_ok = sgqlc.types.Field(Boolean, graphql_name='petsOk')
    windows_ok = sgqlc.types.Field(Boolean, graphql_name='windowsOk')
    laundry_ok = sgqlc.types.Field(Boolean, graphql_name='laundryOk')
    ironing_ok = sgqlc.types.Field(Boolean, graphql_name='ironingOk')


class UserVertical(sgqlc.types.Input):
    __schema__ = helpling_schema
    accept_deliveries = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptDeliveries')
    grocery_shopping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='groceryShopping')
    furniture_assembly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='furnitureAssembly')
    cooking = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='cooking')
    dry_cleaning = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dryCleaning')
    window_cleaning = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='windowCleaning')
    moving_help = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='movingHelp')
    snow_shoveling = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='snowShoveling')
    post_handling = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='postHandling')
    dog_walking = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dogWalking')
    dog_sitting = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dogSitting')
    cat_sitting = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='catSitting')
    pet_feeding = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='petFeeding')
    fish_tank_clean_up = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='fishTankCleanUp')
    watering_plants = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wateringPlants')
    lawn_mowing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='lawnMowing')
    light_yard_work = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='lightYardWork')
    car_washing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='carWashing')
    comment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='comment')


class VerticalSubcategoryInput(sgqlc.types.Input):
    __schema__ = helpling_schema
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    provider_adhoc_price = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='providerAdhocPrice')


class WorkingHourInput(sgqlc.types.Input):
    __schema__ = helpling_schema
    day = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='day')
    open_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='openTime')
    close_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='closeTime')
    available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='available')


########################################################################
# Output Objects and Interfaces
########################################################################
class Address(sgqlc.types.Type):
    __schema__ = helpling_schema
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    address1 = sgqlc.types.Field(String, graphql_name='address1')
    address2 = sgqlc.types.Field(String, graphql_name='address2')
    address_type = sgqlc.types.Field(String, graphql_name='addressType')
    digicode = sgqlc.types.Field(String, graphql_name='digicode')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    floor = sgqlc.types.Field(String, graphql_name='floor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    metro_name = sgqlc.types.Field(String, graphql_name='metroName')
    postcode = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='postcode')
    salutation = sgqlc.types.Field(String, graphql_name='salutation')
    town = sgqlc.types.Field(String, graphql_name='town')


class AdvancedVerificationDocument(sgqlc.types.Type):
    __schema__ = helpling_schema
    checked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checked')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Agency(sgqlc.types.Type):
    __schema__ = helpling_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ApplyPromoMutationResult(sgqlc.types.Type):
    __schema__ = helpling_schema
    message = sgqlc.types.Field(String, graphql_name='message')
    promo = sgqlc.types.Field('Promo', graphql_name='promo')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class BankAccountResultError(sgqlc.types.Type):
    __schema__ = helpling_schema
    bank_acc_number = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='bankAccNumber')
    bank_acc_sortcode = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='bankAccSortcode')
    bank_account_holder = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='bankAccountHolder')
    bank_name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='bankName')
    bic = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='bic')
    bsb = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='bsb')
    iban = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='iban')


class BankTransferType(sgqlc.types.Type):
    __schema__ = helpling_schema
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')
    currency_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currencyType')
    estimated_pay_date = sgqlc.types.Field(DateTime, graphql_name='estimatedPayDate')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    payouts = sgqlc.types.Field(sgqlc.types.list_of('Payout'), graphql_name='payouts')
    provider_charges = sgqlc.types.Field(sgqlc.types.list_of('ProviderCharge'), graphql_name='providerCharges')


class BankTransfersGroupType(sgqlc.types.Type):
    __schema__ = helpling_schema
    bank_transfers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(BankTransferType)),
                                       graphql_name='bankTransfers')
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='date')
    total_amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalAmount')


class Bid(sgqlc.types.Type):
    __schema__ = helpling_schema
    address = sgqlc.types.Field(sgqlc.types.non_null(Address), graphql_name='address')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    distance_from_bid = sgqlc.types.Field(String, graphql_name='distanceFromBid')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='duration', args=sgqlc.types.ArgDict((
        ('unit', sgqlc.types.Arg(TimeUnit, graphql_name='unit', default='SECONDS')),
    ))
                                 )
    end_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endTime')
    frequency = sgqlc.types.Field(String, graphql_name='frequency')
    price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='price', args=sgqlc.types.ArgDict((
        ('format', sgqlc.types.Arg(MoneyFormat, graphql_name='format', default='Plain')),
    ))
                              )
    price_per_hour = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='pricePerHour',
                                       args=sgqlc.types.ArgDict((
                                           ('format',
                                            sgqlc.types.Arg(MoneyFormat, graphql_name='format', default='Plain')),
                                       ))
                                       )
    short_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortAddress')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')
    total_payout = sgqlc.types.Field(String, graphql_name='totalPayout')
    workday_flexibility = sgqlc.types.Field(Boolean, graphql_name='workdayFlexibility')


class BidEdge(sgqlc.types.Type):
    __schema__ = helpling_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(Bid, graphql_name='node')


class BidFlexibility(sgqlc.types.Type):
    __schema__ = helpling_schema
    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')


class Cancellation(sgqlc.types.Type):
    __schema__ = helpling_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_at_with_slashes = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createdAtWithSlashes')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reason_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reasonCode')


class ChangeRequest(sgqlc.types.Type):
    __schema__ = helpling_schema
    address = sgqlc.types.Field(Address, graphql_name='address')
    customer = sgqlc.types.Field('Customer', graphql_name='customer')
    event = sgqlc.types.Field('Event', graphql_name='event')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    next_event = sgqlc.types.Field('Event', graphql_name='nextEvent')
    original_duration = sgqlc.types.Field(Int, graphql_name='originalDuration')
    original_frequency = sgqlc.types.Field(String, graphql_name='originalFrequency')
    original_starttime = sgqlc.types.Field(DateTime, graphql_name='originalStarttime')
    previous_event = sgqlc.types.Field('Event', graphql_name='previousEvent')
    proposed_duration = sgqlc.types.Field(Int, graphql_name='proposedDuration')
    proposed_frequency = sgqlc.types.Field(String, graphql_name='proposedFrequency')
    proposed_starttime = sgqlc.types.Field(DateTime, graphql_name='proposedStarttime')
    provider_response = sgqlc.types.Field(Boolean, graphql_name='providerResponse')


class ChatTermsUpdaterPayload(sgqlc.types.Type):
    __schema__ = helpling_schema
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class Country(sgqlc.types.Type):
    __schema__ = helpling_schema
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CountrySettings(sgqlc.types.Type):
    __schema__ = helpling_schema
    currency = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currency')
    locale = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='locale')
    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')


class CreateAddressResultType(sgqlc.types.Type):
    __schema__ = helpling_schema
    address = sgqlc.types.Field(Address, graphql_name='address')
    error = sgqlc.types.Field(String, graphql_name='error')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CreateCustomerPayload(sgqlc.types.Type):
    __schema__ = helpling_schema
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ErrorType')), graphql_name='errors')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CreateSwissCustomerCommitmentResult(sgqlc.types.Type):
    __schema__ = helpling_schema
    promo = sgqlc.types.Field('Promo', graphql_name='promo')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class CurrentUserInterface(sgqlc.types.Interface):
    __schema__ = helpling_schema
    account_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountType')
    address = sgqlc.types.Field(Address, graphql_name='address')
    chat_terms_agreed_on = sgqlc.types.Field(DateTime, graphql_name='chatTermsAgreedOn')
    firstname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstname')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    preferred_language = sgqlc.types.Field(String, graphql_name='preferredLanguage')


class Customer(sgqlc.types.Type):
    __schema__ = helpling_schema
    address_instructions = sgqlc.types.Field(String, graphql_name='addressInstructions')
    cleaning_details = sgqlc.types.Field(String, graphql_name='cleaningDetails')
    first_event_address = sgqlc.types.Field(Address, graphql_name='firstEventAddress')
    firstname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstname')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    initials = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='initials')
    last_paid_event = sgqlc.types.Field('Event', graphql_name='lastPaidEvent')
    last_rating = sgqlc.types.Field('CustomerRating', graphql_name='lastRating')
    lastname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastname')
    mobile = sgqlc.types.Field(String, graphql_name='mobile')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    next_event = sgqlc.types.Field('Event', graphql_name='nextEvent')
    preferred_language = sgqlc.types.Field(String, graphql_name='preferredLanguage')
    relationship = sgqlc.types.Field('Relationship', graphql_name='relationship')
    requires_payment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresPayment')
    requires_payment_details = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresPaymentDetails')


class CustomerAbTestsType(sgqlc.types.Type):
    __schema__ = helpling_schema
    app_rs_cancellation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='appRsCancellation')


class CustomerBid(sgqlc.types.Type):
    __schema__ = helpling_schema
    address = sgqlc.types.Field(sgqlc.types.non_null(Address), graphql_name='address')
    bid_flexibilities = sgqlc.types.Field(sgqlc.types.list_of(BidFlexibility), graphql_name='bidFlexibilities')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='duration', args=sgqlc.types.ArgDict((
        ('unit', sgqlc.types.Arg(TimeUnit, graphql_name='unit', default='SECONDS')),
    ))
                                 )
    end_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endTime')
    frequency = sgqlc.types.Field(String, graphql_name='frequency')
    max_price = sgqlc.types.Field(Int, graphql_name='maxPrice')
    min_price = sgqlc.types.Field(Int, graphql_name='minPrice')
    payment_error_message = sgqlc.types.Field(String, graphql_name='paymentErrorMessage')
    potential_candidates = sgqlc.types.Field('PotentialCandidateConnection', graphql_name='potentialCandidates',
                                             args=sgqlc.types.ArgDict((
                                                 ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
                                                 ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
                                                 ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
                                                 ('before',
                                                  sgqlc.types.Arg(String, graphql_name='before', default=None)),
                                                 ('sort', sgqlc.types.Arg(CustomerBidPotentialCandidateOrderFields,
                                                                          graphql_name='sort', default='relevance')),
                                                 ('min_price',
                                                  sgqlc.types.Arg(Int, graphql_name='minPrice', default=None)),
                                                 ('max_price',
                                                  sgqlc.types.Arg(Int, graphql_name='maxPrice', default=None)),
                                                 ('min_rating',
                                                  sgqlc.types.Arg(Int, graphql_name='minRating', default=None)),
                                                 ('min_bookings',
                                                  sgqlc.types.Arg(Int, graphql_name='minBookings', default=None)),
                                                 ('pets', sgqlc.types.Arg(Boolean, graphql_name='pets', default=None)),
                                                 ('ironing',
                                                  sgqlc.types.Arg(Boolean, graphql_name='ironing', default=None)),
                                             ))
                                             )
    providers_availability = sgqlc.types.Field(sgqlc.types.list_of('ProvidersAvailabilityType'),
                                               graphql_name='providersAvailability')
    show_interested_providers = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInterestedProviders')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')


class CustomerInvoice(sgqlc.types.Type):
    __schema__ = helpling_schema
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    id = sgqlc.types.Field(ID, graphql_name='id')
    invoice_date = sgqlc.types.Field(Date, graphql_name='invoiceDate')
    paid = sgqlc.types.Field(Boolean, graphql_name='paid')
    paths = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='paths')
    payment_amount = sgqlc.types.Field(Int, graphql_name='paymentAmount')


class CustomerInvoiceEdge(sgqlc.types.Type):
    __schema__ = helpling_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(CustomerInvoice, graphql_name='node')


class DecoratedPotentialCandidateEdge(sgqlc.types.Type):
    __schema__ = helpling_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PotentialCandidateType', graphql_name='node')


class ErrorType(sgqlc.types.Type):
    __schema__ = helpling_schema
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    message = sgqlc.types.Field(String, graphql_name='message')


class Event(sgqlc.types.Type):
    __schema__ = helpling_schema
    address = sgqlc.types.Field(sgqlc.types.non_null(Address), graphql_name='address')
    cancellable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='cancellable')
    cancellation_fee_amount = sgqlc.types.Field(Int, graphql_name='cancellationFeeAmount')
    cancelled = sgqlc.types.Field(Boolean, graphql_name='cancelled')
    cancelled_within_xhours = sgqlc.types.Field(Int, graphql_name='cancelledWithinXHours')
    category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='category')
    change_requests = sgqlc.types.Field(sgqlc.types.list_of(ChangeRequest), graphql_name='changeRequests')
    charge_for_cancellation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='chargeForCancellation')
    clash = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='clash')
    customer = sgqlc.types.Field(Customer, graphql_name='customer')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    eligible_for_cancellation_fee_claim = sgqlc.types.Field(sgqlc.types.non_null(Boolean),
                                                            graphql_name='eligibleForCancellationFeeClaim')
    end_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endTime')
    has_pending_series_change_request = sgqlc.types.Field(Boolean, graphql_name='hasPendingSeriesChangeRequest')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_cleaning = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCleaning')
    is_vertical = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVertical')
    materials = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='materials')
    period = sgqlc.types.Field(String, graphql_name='period')
    post_request_pending = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='postRequestPending')
    prompt_customer_for_conversion = sgqlc.types.Field(sgqlc.types.non_null(Boolean),
                                                       graphql_name='promptCustomerForConversion')
    provider = sgqlc.types.Field('Provider', graphql_name='provider')
    provider_balance = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='providerBalance')
    provider_total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='providerTotal')
    rating = sgqlc.types.Field('CustomerRating', graphql_name='rating')
    relationship = sgqlc.types.Field('Relationship', graphql_name='relationship')
    start_date_with_slashes = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='startDateWithSlashes')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')
    vertical_request = sgqlc.types.Field('VerticalRequestType', graphql_name='verticalRequest')


class EventAmendmentSettings(sgqlc.types.Type):
    __schema__ = helpling_schema
    durations = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='durations')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reasons')
    start_times = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startTimes')


class EventEdge(sgqlc.types.Type):
    __schema__ = helpling_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(Event, graphql_name='node')


class ExperienceAnswerType(sgqlc.types.Type):
    __schema__ = helpling_schema
    human = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='human')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class GeoLocation(sgqlc.types.Type):
    __schema__ = helpling_schema
    lat = sgqlc.types.Field(Float, graphql_name='lat')
    lng = sgqlc.types.Field(Float, graphql_name='lng')


class Holiday(sgqlc.types.Type):
    __schema__ = helpling_schema
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    finish = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='finish')
    id = sgqlc.types.Field(ID, graphql_name='id')
    start = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='start')


class InvoiceType(sgqlc.types.Type):
    __schema__ = helpling_schema
    id = sgqlc.types.Field(ID, graphql_name='id')
    number = sgqlc.types.Field(String, graphql_name='number')
    path = sgqlc.types.Field(String, graphql_name='path')


class Message(sgqlc.types.Type):
    __schema__ = helpling_schema
    body = sgqlc.types.Field(String, graphql_name='body')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    payload = sgqlc.types.Field(sgqlc.types.list_of('payloadRecord'), graphql_name='payload')
    read = sgqlc.types.Field(Boolean, graphql_name='read')
    read_at = sgqlc.types.Field(DateTime, graphql_name='readAt')
    receiver = sgqlc.types.Field('User', graphql_name='receiver')
    receiver_actions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='receiverActions')
    relationship = sgqlc.types.Field('Relationship', graphql_name='relationship')
    sender = sgqlc.types.Field('User', graphql_name='sender')


class MessageEdge(sgqlc.types.Type):
    __schema__ = helpling_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(Message, graphql_name='node')


class MobileVerificationRequiredResult(sgqlc.types.Type):
    __schema__ = helpling_schema
    required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='required')


class Mutation(sgqlc.types.Type):
    __schema__ = helpling_schema
    add_providers_to_bid = sgqlc.types.Field('addProvidersToBidPayload', graphql_name='addProvidersToBid',
                                             args=sgqlc.types.ArgDict((
                                                 ('bid_code',
                                                  sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='bidCode',
                                                                  default=None)),
                                                 ('provider_ids',
                                                  sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                                                                  graphql_name='providerIds', default=None)),
                                                 ('no_selection',
                                                  sgqlc.types.Arg(Boolean, graphql_name='noSelection', default=None)),
                                                 ('instabook',
                                                  sgqlc.types.Arg(Boolean, graphql_name='instabook', default=None)),
                                             ))
                                             )
    agree_chat_terms = sgqlc.types.Field(ChatTermsUpdaterPayload, graphql_name='agreeChatTerms')
    apply_promo = sgqlc.types.Field(ApplyPromoMutationResult, graphql_name='applyPromo', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('promo_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='promoCode', default=None)),
        ('repeat', sgqlc.types.Arg(Boolean, graphql_name='repeat', default=None)),
        ('date', sgqlc.types.Arg(String, graphql_name='date', default=None)),
        ('time', sgqlc.types.Arg(String, graphql_name='time', default=None)),
        ('duration', sgqlc.types.Arg(Int, graphql_name='duration', default=None)),
        ('frequency', sgqlc.types.Arg(String, graphql_name='frequency', default=None)),
    ))
                                    )
    create_customer = sgqlc.types.Field(CreateCustomerPayload, graphql_name='createCustomer', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
        ('firstname', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='firstname', default=None)),
        ('lastname', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='lastname', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
        ('mobile', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mobile', default=None)),
        ('terms', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='terms', default=None)),
    ))
                                        )
    create_public_bid_address = sgqlc.types.Field(CreateAddressResultType, graphql_name='createPublicBidAddress',
                                                  args=sgqlc.types.ArgDict((
                                                      ('bid_code', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                   graphql_name='bidCode',
                                                                                   default=None)),
                                                      ('address1', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                   graphql_name='address1',
                                                                                   default=None)),
                                                      ('address2',
                                                       sgqlc.types.Arg(String, graphql_name='address2', default=None)),
                                                      ('town', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                               graphql_name='town', default=None)),
                                                      ('postcode', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                   graphql_name='postcode',
                                                                                   default=None)),
                                                  ))
                                                  )
    create_swiss_customer_commitment = sgqlc.types.Field(CreateSwissCustomerCommitmentResult,
                                                         graphql_name='createSwissCustomerCommitment',
                                                         args=sgqlc.types.ArgDict((
                                                             ('commitment', sgqlc.types.Arg(
                                                                 sgqlc.types.non_null(CustomerCommitmentEnum),
                                                                 graphql_name='commitment', default=None)),
                                                             ('bid_code', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                          graphql_name='bidCode',
                                                                                          default=None)),
                                                             ('frequency',
                                                              sgqlc.types.Arg(sgqlc.types.non_null(Frequency),
                                                                              graphql_name='frequency', default=None)),
                                                             ('repeat', sgqlc.types.Arg(sgqlc.types.non_null(Boolean),
                                                                                        graphql_name='repeat',
                                                                                        default=None)),
                                                         ))
                                                         )
    customer_assign_bid_to_ab_test = sgqlc.types.Field('MutationGenericResult',
                                                       graphql_name='customerAssignBidToAbTest',
                                                       args=sgqlc.types.ArgDict((
                                                           ('bid_code', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                        graphql_name='bidCode',
                                                                                        default=None)),
                                                           ('experiment_key',
                                                            sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                            graphql_name='experimentKey',
                                                                            default=None)),
                                                           ('group',
                                                            sgqlc.types.Arg(sgqlc.types.non_null(AbTestGroupType),
                                                                            graphql_name='group', default=None)),
                                                       ))
                                                       )
    reactivate_provider_request = sgqlc.types.Field('reactivateProviderResult',
                                                    graphql_name='reactivateProviderRequest')
    remove_promo = sgqlc.types.Field('RemovePromoMutationResult', graphql_name='removePromo', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
    ))
                                     )
    select_candidate = sgqlc.types.Field('SelectCandidateResult', graphql_name='selectCandidate',
                                         args=sgqlc.types.ArgDict((
                                             ('bid_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='bidId',
                                                                        default=None)),
                                             ('candidate_id',
                                              sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='candidateId',
                                                              default=None)),
                                             ('selected',
                                              sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='selected',
                                                              default=None)),
                                         ))
                                         )
    transition_bid_to_provider_selection = sgqlc.types.Field('MutationGenericResult',
                                                             graphql_name='transitionBidToProviderSelection',
                                                             args=sgqlc.types.ArgDict((
                                                                 ('bid_code',
                                                                  sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                  graphql_name='bidCode',
                                                                                  default=None)),
                                                                 ('repeat',
                                                                  sgqlc.types.Arg(Boolean, graphql_name='repeat',
                                                                                  default=None)),
                                                                 ('frequency',
                                                                  sgqlc.types.Arg(Frequency, graphql_name='frequency',
                                                                                  default=None)),
                                                                 ('duration',
                                                                  sgqlc.types.Arg(Int, graphql_name='duration',
                                                                                  default=None)),
                                                                 ('date', sgqlc.types.Arg(String, graphql_name='date',
                                                                                          default=None)),
                                                                 ('time', sgqlc.types.Arg(String, graphql_name='time',
                                                                                          default=None)),
                                                                 ('ironing',
                                                                  sgqlc.types.Arg(Boolean, graphql_name='ironing',
                                                                                  default=None)),
                                                                 ('pets', sgqlc.types.Arg(Boolean, graphql_name='pets',
                                                                                          default=None)),
                                                                 ('materials_required', sgqlc.types.Arg(Boolean,
                                                                                                        graphql_name='materialsRequired',
                                                                                                        default=None)),
                                                                 ('workday_flexibility', sgqlc.types.Arg(Boolean,
                                                                                                         graphql_name='workdayFlexibility',
                                                                                                         default=None)),
                                                                 ('provider_type',
                                                                  sgqlc.types.Arg(String, graphql_name='providerType',
                                                                                  default=None)),
                                                                 ('notes', sgqlc.types.Arg(String, graphql_name='notes',
                                                                                           default=None)),
                                                             ))
                                                             )


class MutationGenericResult(sgqlc.types.Type):
    __schema__ = helpling_schema
    errors = sgqlc.types.Field(sgqlc.types.list_of(ErrorType), graphql_name='errors')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class MyEarnings(sgqlc.types.Type):
    __schema__ = helpling_schema
    current_month_projected = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='currentMonthProjected')
    next_month_projected = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='nextMonthProjected')
    previous_month = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='previousMonth')


class NewRequest(sgqlc.types.Type):
    __schema__ = helpling_schema
    frequency = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='frequency')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    next_event = sgqlc.types.Field(Event, graphql_name='nextEvent')
    payout = sgqlc.types.Field('NewRequestPayout', graphql_name='payout')
    previous_event = sgqlc.types.Field(Event, graphql_name='previousEvent')
    proposed_duration = sgqlc.types.Field(Int, graphql_name='proposedDuration')
    proposed_starttime = sgqlc.types.Field(DateTime, graphql_name='proposedStarttime')
    relationship = sgqlc.types.Field('Relationship', graphql_name='relationship')


class NewRequestPayout(sgqlc.types.Type):
    __schema__ = helpling_schema
    commission_amount_per_hour = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='commissionAmountPerHour')
    price_per_hour = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pricePerHour')
    provider_payout_per_hour = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='providerPayoutPerHour')
    provider_total_payout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='providerTotalPayout')


class Notifications(sgqlc.types.Type):
    __schema__ = helpling_schema
    cancelled_events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='cancelledEvents')
    cancelled_relationships = sgqlc.types.Field(sgqlc.types.list_of('Relationship'),
                                                graphql_name='cancelledRelationships')
    change_requests = sgqlc.types.Field(sgqlc.types.list_of(ChangeRequest), graphql_name='changeRequests')
    count = sgqlc.types.Field(Int, graphql_name='count')
    new_customers = sgqlc.types.Field(sgqlc.types.list_of(Bid), graphql_name='newCustomers')
    new_offers_count = sgqlc.types.Field(Int, graphql_name='newOffersCount')
    new_requests = sgqlc.types.Field(sgqlc.types.list_of(NewRequest), graphql_name='newRequests')
    not_post_agreed_events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='notPostAgreedEvents')
    selected_by_customer = sgqlc.types.Field(sgqlc.types.list_of(Bid), graphql_name='selectedByCustomer')
    today_jobs_count = sgqlc.types.Field(Int, graphql_name='todayJobsCount')
    unconfirmed_events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='unconfirmedEvents')


class OnboardingRequirement(sgqlc.types.Type):
    __schema__ = helpling_schema
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    status = sgqlc.types.Field(sgqlc.types.non_null(OnboardingRequirementStatusEnum), graphql_name='status')


class PageInfo(sgqlc.types.Type):
    __schema__ = helpling_schema
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')


class Payout(sgqlc.types.Type):
    __schema__ = helpling_schema
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')
    customer_name = sgqlc.types.Field(String, graphql_name='customerName')
    event = sgqlc.types.Field(Event, graphql_name='event')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    paid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='paid')


class PendingFundsPayout(sgqlc.types.Type):
    __schema__ = helpling_schema
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')
    customer_name = sgqlc.types.Field(String, graphql_name='customerName')
    event = sgqlc.types.Field(Event, graphql_name='event')
    funds_available_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='fundsAvailableOn')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class PostCleanRequest(sgqlc.types.Type):
    __schema__ = helpling_schema
    action_required_by = sgqlc.types.Field(String, graphql_name='actionRequiredBy')
    actioned = sgqlc.types.Field(Boolean, graphql_name='actioned')
    actioned_by = sgqlc.types.Field(Int, graphql_name='actionedBy')
    cancellation_reason_code = sgqlc.types.Field(String, graphql_name='cancellationReasonCode')
    cancelled = sgqlc.types.Field(Int, graphql_name='cancelled')
    change_type = sgqlc.types.Field(String, graphql_name='changeType')
    created_by = sgqlc.types.Field(Int, graphql_name='createdBy')
    customer_response = sgqlc.types.Field(Boolean, graphql_name='customerResponse')
    email_link_id = sgqlc.types.Field(String, graphql_name='emailLinkId')
    event_id = sgqlc.types.Field(Int, graphql_name='eventId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_first_in_relationship = sgqlc.types.Field(Boolean, graphql_name='isFirstInRelationship')
    is_first_in_series = sgqlc.types.Field(Boolean, graphql_name='isFirstInSeries')
    original_duration = sgqlc.types.Field(Int, graphql_name='originalDuration')
    original_starttime = sgqlc.types.Field(DateTime, graphql_name='originalStarttime')
    other_response = sgqlc.types.Field(String, graphql_name='otherResponse')
    proposed_duration = sgqlc.types.Field(Int, graphql_name='proposedDuration')
    proposed_starttime = sgqlc.types.Field(DateTime, graphql_name='proposedStarttime')
    provider_agreed_with_customer = sgqlc.types.Field(Boolean, graphql_name='providerAgreedWithCustomer')


class PostCode(sgqlc.types.Type):
    __schema__ = helpling_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class PotentialCandidateConnection(sgqlc.types.relay.Connection):
    __schema__ = helpling_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of(DecoratedPotentialCandidateEdge), graphql_name='edges')
    maximum_price_filter = sgqlc.types.Field(Int, graphql_name='maximumPriceFilter')
    minimum_price_filter = sgqlc.types.Field(Int, graphql_name='minimumPriceFilter')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')


class PotentialCandidateType(sgqlc.types.Type):
    __schema__ = helpling_schema
    price_per_hour = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='pricePerHour',
                                       args=sgqlc.types.ArgDict((
                                           ('format',
                                            sgqlc.types.Arg(MoneyFormat, graphql_name='format', default='Plain')),
                                       ))
                                       )
    provider = sgqlc.types.Field('Provider', graphql_name='provider')


class Promo(sgqlc.types.Type):
    __schema__ = helpling_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oneoff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='oneoff')
    promo_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='promoCode')
    repeat = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='repeat')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    value_type = sgqlc.types.Field(PromoValueType, graphql_name='valueType')


class Provider(sgqlc.types.Type):
    __schema__ = helpling_schema
    accepts_new_bookings = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptsNewBookings')
    accepts_new_requests = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptsNewRequests')
    advanced_documents = sgqlc.types.Field(sgqlc.types.list_of(AdvancedVerificationDocument),
                                           graphql_name='advancedDocuments')
    agency = sgqlc.types.Field(Agency, graphql_name='agency')
    avg_rating = sgqlc.types.Field('ProviderAvgRating', graphql_name='avgRating', args=sgqlc.types.ArgDict((
        ('precision', sgqlc.types.Arg(Int, graphql_name='precision', default=2)),
    ))
                                   )
    awaiting_onfido_pass = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='awaitingOnfidoPass')
    best_rating_received = sgqlc.types.Field('ProviderRating', graphql_name='bestRatingReceived')
    bid_preferences = sgqlc.types.Field('bidPreferences', graphql_name='bidPreferences')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_adhoc_price = sgqlc.types.Field(String, graphql_name='customerAdhocPrice')
    customer_repeat_price = sgqlc.types.Field(String, graphql_name='customerRepeatPrice')
    default_profile_image = sgqlc.types.Field(String, graphql_name='defaultProfileImage')
    display_restructuring_note = sgqlc.types.Field(Boolean, graphql_name='displayRestructuringNote')
    distance_to_bid = sgqlc.types.Field(Float, graphql_name='distanceToBid', args=sgqlc.types.ArgDict((
        ('bid_code', sgqlc.types.Arg(String, graphql_name='bidCode', default=None)),
    ))
                                        )
    documents = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='documents')
    eligible_for_training_certificate = sgqlc.types.Field(Boolean, graphql_name='eligibleForTrainingCertificate')
    event = sgqlc.types.Field(Event, graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                              )
    experience = sgqlc.types.Field('experienceType', graphql_name='experience')
    finished_events_count = sgqlc.types.Field(Int, graphql_name='finishedEventsCount')
    firstname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstname')
    future_holidays = sgqlc.types.Field(sgqlc.types.list_of(Holiday), graphql_name='futureHolidays')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image = sgqlc.types.Field(String, graphql_name='image')
    in_active_relationship = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='inActiveRelationship')
    in_agency = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='inAgency')
    instabook_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='instabookEnabled')
    ironing = sgqlc.types.Field(Boolean, graphql_name='ironing')
    language_skills = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='languageSkills')
    lastname = sgqlc.types.Field(String, graphql_name='lastname')
    live = sgqlc.types.Field(Boolean, graphql_name='live')
    metro = sgqlc.types.Field(String, graphql_name='metro')
    mobile = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mobile')
    my_earnings = sgqlc.types.Field(MyEarnings, graphql_name='myEarnings')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nationality = sgqlc.types.Field(String, graphql_name='nationality')
    notification_message = sgqlc.types.Field('ProviderNotificationMessageType', graphql_name='notificationMessage')
    notifications = sgqlc.types.Field(Notifications, graphql_name='notifications')
    onboarding_requirements = sgqlc.types.Field(sgqlc.types.list_of(OnboardingRequirement),
                                                graphql_name='onboardingRequirements')
    peer_providers = sgqlc.types.Field(sgqlc.types.list_of('Provider'), graphql_name='peerProviders')
    performance = sgqlc.types.Field('ProviderPerformance', graphql_name='performance')
    performed_cleanings_count = sgqlc.types.Field(Int, graphql_name='performedCleaningsCount')
    pets = sgqlc.types.Field(Boolean, graphql_name='pets')
    price_recommendations = sgqlc.types.Field('priceRecommendations', graphql_name='priceRecommendations')
    prices = sgqlc.types.Field('prices', graphql_name='prices')
    profile = sgqlc.types.Field('ProviderProfile', graphql_name='profile')
    profile_image = sgqlc.types.Field(String, graphql_name='profileImage')
    provider_adhoc_price = sgqlc.types.Field(String, graphql_name='providerAdhocPrice')
    provider_areas = sgqlc.types.Field(sgqlc.types.list_of('ProviderArea'), graphql_name='providerAreas')
    provider_driven_cancelled_relationships = sgqlc.types.Field(sgqlc.types.list_of('Relationship'),
                                                                graphql_name='providerDrivenCancelledRelationships',
                                                                args=sgqlc.types.ArgDict((
                                                                    ('from_time',
                                                                     sgqlc.types.Arg(DateTime, graphql_name='fromTime',
                                                                                     default=None)),
                                                                    ('to_time',
                                                                     sgqlc.types.Arg(DateTime, graphql_name='toTime',
                                                                                     default=None)),
                                                                ))
                                                                )
    provider_repeat_price = sgqlc.types.Field(String, graphql_name='providerRepeatPrice')
    public_profile_image = sgqlc.types.Field(String, graphql_name='publicProfileImage')
    rating = sgqlc.types.Field(Float, graphql_name='rating')
    ratings = sgqlc.types.Field('ProviderRatingConnectionType', graphql_name='ratings', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('unread', sgqlc.types.Arg(Boolean, graphql_name='unread', default=False)),
        ('readable', sgqlc.types.Arg(Boolean, graphql_name='readable', default=False)),
        ('live', sgqlc.types.Arg(Boolean, graphql_name='live', default=False)),
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
        ('references', sgqlc.types.Arg(Boolean, graphql_name='references', default=False)),
        ('date_time_order', sgqlc.types.Arg(OrderDirection, graphql_name='dateTimeOrder', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('category', sgqlc.types.Arg(String, graphql_name='category', default='cleaning.home')),
    ))
                                )
    ratings_counts_per_category = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null('ProviderRatingCountPerCategory')),
        graphql_name='ratingsCountsPerCategory')
    ratings_histogram = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProviderRatingStarsCount'))),
        graphql_name='ratingsHistogram', args=sgqlc.types.ArgDict((
            ('category', sgqlc.types.Arg(String, graphql_name='category', default='cleaning.home')),
        ))
        )
    ratings_received_count = sgqlc.types.Field(Int, graphql_name='ratingsReceivedCount')
    references_code = sgqlc.types.Field(String, graphql_name='referencesCode')
    shortname = sgqlc.types.Field(String, graphql_name='shortname')
    stats = sgqlc.types.Field('ProviderStats', graphql_name='stats')
    stripe_account = sgqlc.types.Field('ProviderStripeAccount', graphql_name='stripeAccount')
    successful_events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='successfulEvents',
                                          args=sgqlc.types.ArgDict((
                                              ('from_time',
                                               sgqlc.types.Arg(DateTime, graphql_name='fromTime', default=None)),
                                              ('to_time',
                                               sgqlc.types.Arg(DateTime, graphql_name='toTime', default=None)),
                                          ))
                                          )
    tax_certificates = sgqlc.types.Field(sgqlc.types.list_of('TaxCertificate'), graphql_name='taxCertificates')
    unread_messages_count = sgqlc.types.Field(Int, graphql_name='unreadMessagesCount')
    verification_level = sgqlc.types.Field(String, graphql_name='verificationLevel')
    vertical_services = sgqlc.types.Field(sgqlc.types.list_of('ProviderVerticalServiceType'),
                                          graphql_name='verticalServices')
    vertical_stats = sgqlc.types.Field('ProviderVerticalStats', graphql_name='verticalStats', args=sgqlc.types.ArgDict((
        ('category', sgqlc.types.Arg(String, graphql_name='category', default=None)),
    ))
                                       )
    welcome_call = sgqlc.types.Field('ProviderWelcomeCallType', graphql_name='welcomeCall')
    windows = sgqlc.types.Field(Boolean, graphql_name='windows')
    work_location = sgqlc.types.Field(GeoLocation, graphql_name='workLocation')
    work_status = sgqlc.types.Field(String, graphql_name='workStatus')


class ProviderAppAbTestsType(sgqlc.types.Type):
    __schema__ = helpling_schema
    skip_provider_intro_fee = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='skipProviderIntroFee')


class ProviderAppFeatureFlagsType(sgqlc.types.Type):
    __schema__ = helpling_schema
    mediator_model = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mediatorModel')
    psd2_payments = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='psd2Payments')
    require_in_house_training = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requireInHouseTraining')
    show_confirmed_events_per_month = sgqlc.types.Field(sgqlc.types.non_null(Boolean),
                                                        graphql_name='showConfirmedEventsPerMonth')
    show_hotline_info = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showHotlineInfo')
    tax_id_in_profile_form = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxIdInProfileForm')
    vertical_offers = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='verticalOffers')
    vertical_services = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='verticalServices')


class ProviderArea(sgqlc.types.Type):
    __schema__ = helpling_schema
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    postcode = sgqlc.types.Field(PostCode, graphql_name='postcode')


class ProviderBusySlotType(sgqlc.types.Type):
    __schema__ = helpling_schema
    end_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endTime')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')
    type = sgqlc.types.Field(sgqlc.types.non_null(BusySlotType), graphql_name='type')


class ProviderCharge(sgqlc.types.Type):
    __schema__ = helpling_schema
    charge_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chargeType')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Provider), graphql_name='provider')
    total = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='total')


class ProviderNotificationMessageType(sgqlc.types.Type):
    __schema__ = helpling_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    translation_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='translationKey')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class ProviderPerformance(sgqlc.types.Type):
    __schema__ = helpling_schema
    cancelled_events_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cancelledEventsCount')
    days_active_on_platform = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='daysActiveOnPlatform')
    relationships_longer_than3_months_count = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                                graphql_name='relationshipsLongerThan3MonthsCount')
    score = sgqlc.types.Field(Int, graphql_name='score')
    successful_events_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successfulEventsCount')


class ProviderProfile(sgqlc.types.Type):
    __schema__ = helpling_schema
    ironing_ok = sgqlc.types.Field(Boolean, graphql_name='ironingOk')
    laundry_ok = sgqlc.types.Field(Boolean, graphql_name='laundryOk')
    pets_ok = sgqlc.types.Field(Boolean, graphql_name='petsOk')
    tax_id = sgqlc.types.Field(String, graphql_name='taxId')
    vat_id = sgqlc.types.Field(String, graphql_name='vatId')
    windows_ok = sgqlc.types.Field(Boolean, graphql_name='windowsOk')


class ProviderRatingConnectionType(sgqlc.types.Type):
    __schema__ = helpling_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProviderRatingEdge'), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')


class ProviderRatingCountPerCategory(sgqlc.types.Type):
    __schema__ = helpling_schema
    category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='category')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')


class ProviderRatingEdge(sgqlc.types.Type):
    __schema__ = helpling_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProviderRating', graphql_name='node')


class ProviderRatingStarsCount(sgqlc.types.Type):
    __schema__ = helpling_schema
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    stars = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='stars')


class ProviderStats(sgqlc.types.Type):
    __schema__ = helpling_schema
    jobs_done = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='jobsDone')
    jobs_done_percentage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='jobsDonePercentage')
    rating_percentage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ratingPercentage')
    responded = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='responded')
    responded_percentage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='respondedPercentage')


class ProviderStripeAccount(sgqlc.types.Type):
    __schema__ = helpling_schema
    charges_enabled = sgqlc.types.Field(Boolean, graphql_name='chargesEnabled')
    id_verification_required = sgqlc.types.Field(Boolean, graphql_name='idVerificationRequired')
    payouts_enabled = sgqlc.types.Field(Boolean, graphql_name='payoutsEnabled')
    verification_deadline = sgqlc.types.Field(DateTime, graphql_name='verificationDeadline')


class ProviderTypesCategories(sgqlc.types.Type):
    __schema__ = helpling_schema
    agency = sgqlc.types.Field('ProviderTypesDetails', graphql_name='agency')
    best_priced = sgqlc.types.Field('ProviderTypesDetails', graphql_name='bestPriced')
    top_rated = sgqlc.types.Field('ProviderTypesDetails', graphql_name='topRated')


class ProviderTypesDetails(sgqlc.types.Type):
    __schema__ = helpling_schema
    adhoc = sgqlc.types.Field('SettingsProviderTypePrices', graphql_name='adhoc')
    repeat = sgqlc.types.Field('SettingsProviderTypePrices', graphql_name='repeat')


class ProviderVerticalPriceSettingType(sgqlc.types.Type):
    __schema__ = helpling_schema
    category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='category')
    pricing_unit = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pricingUnit')
    provider_adhoc_price = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='providerAdhocPrice')
    suggested_price = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='suggestedPrice')


class ProviderVerticalPricingUnitType(sgqlc.types.Type):
    __schema__ = helpling_schema
    category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='category')
    pricing_unit = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pricingUnit')


class ProviderVerticalServiceType(sgqlc.types.Type):
    __schema__ = helpling_schema
    category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='category')
    description = sgqlc.types.Field(String, graphql_name='description')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    id = sgqlc.types.Field(ID, graphql_name='id')
    provider_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='providerId')
    subcategories = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProviderVerticalSubcategoryType'))),
        graphql_name='subcategories')


class ProviderVerticalStats(sgqlc.types.Type):
    __schema__ = helpling_schema
    completed_events_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='completedEventsCount')
    ratings_received_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ratingsReceivedCount')


class ProviderVerticalSubcategoryType(sgqlc.types.Type):
    __schema__ = helpling_schema
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    price_setting = sgqlc.types.Field(sgqlc.types.non_null(ProviderVerticalPriceSettingType),
                                      graphql_name='priceSetting')


class ProviderWelcomeCallType(sgqlc.types.Type):
    __schema__ = helpling_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    occurred_at = sgqlc.types.Field(DateTime, graphql_name='occurredAt')
    preferred_time = sgqlc.types.Field(String, graphql_name='preferredTime')


class ProvidersAvailabilityType(sgqlc.types.Type):
    __schema__ = helpling_schema
    cleaners_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cleanersCount')
    date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='date')


class Query(sgqlc.types.Type):
    __schema__ = helpling_schema
    category_available_in_postcode = sgqlc.types.Field(sgqlc.types.non_null(Boolean),
                                                       graphql_name='categoryAvailableInPostcode',
                                                       args=sgqlc.types.ArgDict((
                                                           ('postcode', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                        graphql_name='postcode',
                                                                                        default=None)),
                                                           ('category', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                        graphql_name='category',
                                                                                        default=None)),
                                                       ))
                                                       )
    cleaners_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cleanersCount')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_at_with_slashes = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createdAtWithSlashes')
    current_user = sgqlc.types.Field(CurrentUserInterface, graphql_name='currentUser')
    customer = sgqlc.types.Field(Customer, graphql_name='customer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                                 )
    customer_bid = sgqlc.types.Field(CustomerBid, graphql_name='customerBid', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(String, graphql_name='code', default=None)),
    ))
                                     )
    date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='date')
    find_vertical_request_candidates = sgqlc.types.Field(sgqlc.types.list_of(Provider),
                                                         graphql_name='findVerticalRequestCandidates',
                                                         args=sgqlc.types.ArgDict((
                                                             ('category', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                          graphql_name='category',
                                                                                          default=None)),
                                                             ('starttime',
                                                              sgqlc.types.Arg(sgqlc.types.non_null(DateTime),
                                                                              graphql_name='starttime', default=None)),
                                                             ('frequency', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                           graphql_name='frequency',
                                                                                           default=None)),
                                                             ('duration', sgqlc.types.Arg(sgqlc.types.non_null(Int),
                                                                                          graphql_name='duration',
                                                                                          default=None)),
                                                             ('postcode',
                                                              sgqlc.types.Arg(String, graphql_name='postcode',
                                                                              default=None)),
                                                         ))
                                                         )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    mobile_verification_required = sgqlc.types.Field(MobileVerificationRequiredResult,
                                                     graphql_name='mobileVerificationRequired')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Provider), graphql_name='provider', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                                 )
    reason_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reasonCode')
    settings = sgqlc.types.Field('settings', graphql_name='settings')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')


class QueryExpeditedPaymentResult(sgqlc.types.Type):
    __schema__ = helpling_schema
    balance = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='balance')
    commission = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='commission')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')


class Rating(sgqlc.types.Interface):
    __schema__ = helpling_schema
    communication = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='communication')
    quality = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='quality')
    reliability = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='reliability')
    total = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='total')


class Relationship(sgqlc.types.Type):
    __schema__ = helpling_schema
    address = sgqlc.types.Field(Address, graphql_name='address')
    cancellation = sgqlc.types.Field(Cancellation, graphql_name='cancellation')
    cancellation_reason_code = sgqlc.types.Field(String, graphql_name='cancellationReasonCode')
    cancelled = sgqlc.types.Field(Boolean, graphql_name='cancelled')
    cancelled_at = sgqlc.types.Field(String, graphql_name='cancelledAt')
    cancelled_at_with_slashes = sgqlc.types.Field(String, graphql_name='cancelledAtWithSlashes')
    customer = sgqlc.types.Field(sgqlc.types.non_null(Customer), graphql_name='customer')
    customer_recurring_price = sgqlc.types.Field(Int, graphql_name='customerRecurringPrice')
    future_events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='futureEvents',
                                      args=sgqlc.types.ArgDict((
                                          ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=4)),
                                          ('after_start_time',
                                           sgqlc.types.Arg(DateTime, graphql_name='afterStartTime', default=None)),
                                          ('cancelled',
                                           sgqlc.types.Arg(Boolean, graphql_name='cancelled', default=None)),
                                      ))
                                      )
    has_only_one_off_events = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasOnlyOneOffEvents')
    has_pending_automated_cancellation = sgqlc.types.Field(Boolean, graphql_name='hasPendingAutomatedCancellation')
    has_pending_cancellation = sgqlc.types.Field(Boolean, graphql_name='hasPendingCancellation')
    has_pending_price_change_request = sgqlc.types.Field(sgqlc.types.non_null(Boolean),
                                                         graphql_name='hasPendingPriceChangeRequest')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    last_live_past_post_agreed = sgqlc.types.Field(Event, graphql_name='lastLivePastPostAgreed')
    last_past_event = sgqlc.types.Field(Event, graphql_name='lastPastEvent')
    latest_event = sgqlc.types.Field(Event, graphql_name='latestEvent')
    past_booking_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pastBookingCount')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Provider), graphql_name='provider')
    provider_average_rating = sgqlc.types.Field(Float, graphql_name='providerAverageRating', args=sgqlc.types.ArgDict((
        ('precision', sgqlc.types.Arg(Int, graphql_name='precision', default=1)),
    ))
                                                )
    provider_recurring_price = sgqlc.types.Field(Int, graphql_name='providerRecurringPrice')
    series = sgqlc.types.Field(sgqlc.types.list_of('Series'), graphql_name='series')
    successful_events_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successfulEventsCount')


class RemovePromoMutationResult(sgqlc.types.Type):
    __schema__ = helpling_schema
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class SelectCandidateResult(sgqlc.types.Type):
    __schema__ = helpling_schema
    error = sgqlc.types.Field(String, graphql_name='error')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class Series(sgqlc.types.Type):
    __schema__ = helpling_schema
    change_requestable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='changeRequestable')
    change_requests = sgqlc.types.Field(sgqlc.types.list_of(ChangeRequest), graphql_name='changeRequests')
    day = sgqlc.types.Field(Int, graphql_name='day')
    duration = sgqlc.types.Field(Int, graphql_name='duration')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    live = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='live')
    period = sgqlc.types.Field(String, graphql_name='period')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')


class SettingsCandidateType(sgqlc.types.Type):
    __schema__ = helpling_schema
    active_relationships_count = sgqlc.types.Field(Int, graphql_name='activeRelationshipsCount')
    average_rating = sgqlc.types.Field(Float, graphql_name='averageRating')
    average_rating_float = sgqlc.types.Field(Float, graphql_name='averageRatingFloat')
    best_rating_received = sgqlc.types.Field('bestRatingReceived', graphql_name='bestRatingReceived')
    documents = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='documents')
    experience_description = sgqlc.types.Field(String, graphql_name='experienceDescription')
    experience_headline = sgqlc.types.Field(String, graphql_name='experienceHeadline')
    firstname = sgqlc.types.Field(String, graphql_name='firstname')
    gender = sgqlc.types.Field(String, graphql_name='gender')
    golive_date = sgqlc.types.Field(DateTime, graphql_name='goliveDate')
    id = sgqlc.types.Field(Int, graphql_name='id')
    ironing = sgqlc.types.Field(Boolean, graphql_name='ironing')
    language_skills = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='languageSkills')
    lastname = sgqlc.types.Field(String, graphql_name='lastname')
    laundry = sgqlc.types.Field(Boolean, graphql_name='laundry')
    performance_score = sgqlc.types.Field(Float, graphql_name='performanceScore')
    performed_cleanings_count = sgqlc.types.Field(Int, graphql_name='performedCleaningsCount')
    pets = sgqlc.types.Field(Boolean, graphql_name='pets')
    picture = sgqlc.types.Field(String, graphql_name='picture')
    price_per_hour = sgqlc.types.Field(Int, graphql_name='pricePerHour')
    profile_image = sgqlc.types.Field(String, graphql_name='profileImage')
    ratings_received_count = sgqlc.types.Field(Int, graphql_name='ratingsReceivedCount')
    selected = sgqlc.types.Field(Boolean, graphql_name='selected')
    shortname = sgqlc.types.Field(String, graphql_name='shortname')
    top_value = sgqlc.types.Field(Boolean, graphql_name='topValue')
    user_id = sgqlc.types.Field(Int, graphql_name='userId')
    verification_level = sgqlc.types.Field(String, graphql_name='verificationLevel')
    windows = sgqlc.types.Field(Boolean, graphql_name='windows')


class SettingsDesktopCheckoutApi(sgqlc.types.Type):
    __schema__ = helpling_schema
    base_url = sgqlc.types.Field(String, graphql_name='baseUrl')


class SettingsDesktopCheckoutBid(sgqlc.types.Type):
    __schema__ = helpling_schema
    address_id = sgqlc.types.Field(Int, graphql_name='addressId')
    date = sgqlc.types.Field(DateTime, graphql_name='date')
    duration = sgqlc.types.Field('SettingsTimePropType', graphql_name='duration')
    frequency = sgqlc.types.Field(String, graphql_name='frequency')
    identifier = sgqlc.types.Field(String, graphql_name='identifier')
    promo = sgqlc.types.Field('SettingsDesktopCheckoutBidPromo', graphql_name='promo')
    replacement_for_type = sgqlc.types.Field(String, graphql_name='replacementForType')
    time = sgqlc.types.Field('SettingsTimePropType', graphql_name='time')


class SettingsDesktopCheckoutBidPromo(sgqlc.types.Type):
    __schema__ = helpling_schema
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    code = sgqlc.types.Field(String, graphql_name='code')
    expires_at = sgqlc.types.Field(Date, graphql_name='expiresAt')
    max_usage_count = sgqlc.types.Field(Int, graphql_name='maxUsageCount')
    min_hours = sgqlc.types.Field(Int, graphql_name='minHours')
    one_off = sgqlc.types.Field(Boolean, graphql_name='oneOff')
    only_new_customer = sgqlc.types.Field(Boolean, graphql_name='onlyNewCustomer')
    repeat = sgqlc.types.Field(Boolean, graphql_name='repeat')
    services = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='services')
    starts_at = sgqlc.types.Field(Date, graphql_name='startsAt')
    usage_count = sgqlc.types.Field(Int, graphql_name='usageCount')
    value = sgqlc.types.Field(Int, graphql_name='value')
    value_type = sgqlc.types.Field(String, graphql_name='valueType')


class SettingsDesktopCheckoutCandidates(sgqlc.types.Type):
    __schema__ = helpling_schema
    data = sgqlc.types.Field(sgqlc.types.list_of(SettingsCandidateType), graphql_name='data')


class SettingsDesktopCheckoutComponents(sgqlc.types.Type):
    __schema__ = helpling_schema
    date = sgqlc.types.Field('SettingsDesktopCheckoutComponentsDate', graphql_name='date')
    duration = sgqlc.types.Field('SettingsDesktopCheckoutComponentsDuration', graphql_name='duration')
    extras = sgqlc.types.Field('SettingsDesktopCheckoutComponentsExtras', graphql_name='extras')
    frequency = sgqlc.types.Field('SettingsDesktopCheckoutComponentsFrequency', graphql_name='frequency')
    payments = sgqlc.types.Field('SettingsDesktopCheckoutComponentsPayments', graphql_name='payments')
    time = sgqlc.types.Field('SettingsDesktopCheckoutComponentsTime', graphql_name='time')


class SettingsDesktopCheckoutComponentsDate(sgqlc.types.Type):
    __schema__ = helpling_schema
    default = sgqlc.types.Field(Date, graphql_name='default')
    props = sgqlc.types.Field('SettingsDesktopCheckoutComponentsDateProps', graphql_name='props')


class SettingsDesktopCheckoutComponentsDateProps(sgqlc.types.Type):
    __schema__ = helpling_schema
    default_day = sgqlc.types.Field(Int, graphql_name='defaultDay')
    disabled_days = sgqlc.types.Field(Int, graphql_name='disabledDays')


class SettingsDesktopCheckoutComponentsDuration(sgqlc.types.Type):
    __schema__ = helpling_schema
    default = sgqlc.types.Field('SettingsDesktopCheckoutComponentsDurationDefault', graphql_name='default')
    props = sgqlc.types.Field('SettingsDesktopCheckoutComponentsDurationProps', graphql_name='props')


class SettingsDesktopCheckoutComponentsDurationDefault(sgqlc.types.Type):
    __schema__ = helpling_schema
    one_off = sgqlc.types.Field('SettingsTimePropType', graphql_name='oneOff')
    recurring = sgqlc.types.Field('SettingsTimePropType', graphql_name='recurring')


class SettingsDesktopCheckoutComponentsDurationProps(sgqlc.types.Type):
    __schema__ = helpling_schema
    one_off = sgqlc.types.Field('SettingsDesktopCheckoutComponentsDurationPropsOneOff', graphql_name='oneOff')
    recurring = sgqlc.types.Field('SettingsDesktopCheckoutComponentsDurationPropsRecurring', graphql_name='recurring')


class SettingsDesktopCheckoutComponentsDurationPropsOneOff(sgqlc.types.Type):
    __schema__ = helpling_schema
    hidden_options = sgqlc.types.Field(sgqlc.types.list_of('SettingsTimePropType'), graphql_name='hiddenOptions')
    visible_options = sgqlc.types.Field(sgqlc.types.list_of('SettingsTimePropType'), graphql_name='visibleOptions')


class SettingsDesktopCheckoutComponentsDurationPropsRecurring(sgqlc.types.Type):
    __schema__ = helpling_schema
    hidden_options = sgqlc.types.Field(sgqlc.types.list_of('SettingsTimePropType'), graphql_name='hiddenOptions')
    visible_options = sgqlc.types.Field(sgqlc.types.list_of('SettingsTimePropType'), graphql_name='visibleOptions')


class SettingsDesktopCheckoutComponentsExtras(sgqlc.types.Type):
    __schema__ = helpling_schema
    default = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='default')
    props = sgqlc.types.Field('SettingsDesktopCheckoutComponentsExtrasProps', graphql_name='props')


class SettingsDesktopCheckoutComponentsExtrasProps(sgqlc.types.Type):
    __schema__ = helpling_schema
    items = sgqlc.types.Field(sgqlc.types.list_of('SettingsDesktopCheckoutComponentsExtrasPropsItems'),
                              graphql_name='items')


class SettingsDesktopCheckoutComponentsExtrasPropsItems(sgqlc.types.Type):
    __schema__ = helpling_schema
    badge = sgqlc.types.Field(String, graphql_name='badge')
    label = sgqlc.types.Field(String, graphql_name='label')
    name = sgqlc.types.Field(String, graphql_name='name')
    price_one_off = sgqlc.types.Field(Int, graphql_name='priceOneOff')
    price_recurring = sgqlc.types.Field(Int, graphql_name='priceRecurring')
    time = sgqlc.types.Field(Int, graphql_name='time')


class SettingsDesktopCheckoutComponentsFrequency(sgqlc.types.Type):
    __schema__ = helpling_schema
    default = sgqlc.types.Field(String, graphql_name='default')
    props = sgqlc.types.Field('SettingsDesktopCheckoutComponentsFrequencyProps', graphql_name='props')


class SettingsDesktopCheckoutComponentsFrequencyProps(sgqlc.types.Type):
    __schema__ = helpling_schema
    once_off_int = sgqlc.types.Field(Int, graphql_name='onceOffInt')
    one_off_price = sgqlc.types.Field(String, graphql_name='oneOffPrice')
    recurring_int = sgqlc.types.Field(Int, graphql_name='recurringInt')
    recurring_price = sgqlc.types.Field(String, graphql_name='recurringPrice')
    repeat_discount = sgqlc.types.Field(Int, graphql_name='repeatDiscount')


class SettingsDesktopCheckoutComponentsPayments(sgqlc.types.Type):
    __schema__ = helpling_schema
    props = sgqlc.types.Field('SettingsDesktopCheckoutComponentsPaymentsProps', graphql_name='props')


class SettingsDesktopCheckoutComponentsPaymentsProps(sgqlc.types.Type):
    __schema__ = helpling_schema
    methods = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='methods')


class SettingsDesktopCheckoutComponentsTime(sgqlc.types.Type):
    __schema__ = helpling_schema
    default = sgqlc.types.Field('SettingsTimePropType', graphql_name='default')
    props = sgqlc.types.Field('SettingsDesktopCheckoutComponentsTimeProps', graphql_name='props')


class SettingsDesktopCheckoutComponentsTimeProps(sgqlc.types.Type):
    __schema__ = helpling_schema
    options = sgqlc.types.Field(sgqlc.types.list_of('SettingsTimePropType'), graphql_name='options')


class SettingsDesktopCheckoutCountry(sgqlc.types.Type):
    __schema__ = helpling_schema
    am_pm = sgqlc.types.Field(Boolean, graphql_name='amPm')
    available_locales = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='availableLocales')
    country = sgqlc.types.Field(String, graphql_name='country')
    currency_code = sgqlc.types.Field(String, graphql_name='currencyCode')
    customer_marketplace_fee = sgqlc.types.Field(Int, graphql_name='customerMarketplaceFee')
    customer_marketplace_fee_enabled = sgqlc.types.Field(Boolean, graphql_name='customerMarketplaceFeeEnabled')
    customer_peak_fee = sgqlc.types.Field(Int, graphql_name='customerPeakFee')
    customer_peak_fee_days = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='customerPeakFeeDays')
    customer_peak_fee_enabled = sgqlc.types.Field(Boolean, graphql_name='customerPeakFeeEnabled')
    ideal_authorisation_amount = sgqlc.types.Field(Int, graphql_name='idealAuthorisationAmount')
    locale = sgqlc.types.Field(String, graphql_name='locale')
    metro = sgqlc.types.Field(String, graphql_name='metro')
    moment_locale = sgqlc.types.Field(String, graphql_name='momentLocale')
    multi_language = sgqlc.types.Field(String, graphql_name='multiLanguage')
    multi_lingual_support = sgqlc.types.Field(Boolean, graphql_name='multiLingualSupport')
    provider_availability = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)),
                                              graphql_name='providerAvailability')
    provider_default_filters = sgqlc.types.Field('countryProviderDefaultFilters', graphql_name='providerDefaultFilters')
    time_format = sgqlc.types.Field(String, graphql_name='timeFormat')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')


class SettingsDesktopCheckoutCustomer(sgqlc.types.Type):
    __schema__ = helpling_schema
    address = sgqlc.types.Field('SettingsDesktopCheckoutCustomerAddress', graphql_name='address')
    email = sgqlc.types.Field(String, graphql_name='email')
    firstname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstname')
    has_converted = sgqlc.types.Field(Boolean, graphql_name='hasConverted')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    lastname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastname')
    preferred_language = sgqlc.types.Field(String, graphql_name='preferredLanguage')
    requires_payment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresPayment')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class SettingsDesktopCheckoutCustomerAddress(sgqlc.types.Type):
    __schema__ = helpling_schema
    address1 = sgqlc.types.Field(String, graphql_name='address1')
    address2 = sgqlc.types.Field(String, graphql_name='address2')
    address_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='addressType')
    digicode = sgqlc.types.Field(String, graphql_name='digicode')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    floor = sgqlc.types.Field(String, graphql_name='floor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    postcode = sgqlc.types.Field(String, graphql_name='postcode')
    salutation = sgqlc.types.Field(String, graphql_name='salutation')
    town = sgqlc.types.Field(String, graphql_name='town')


class SettingsDesktopCheckoutDevice(sgqlc.types.Type):
    __schema__ = helpling_schema
    is_mobile = sgqlc.types.Field(Boolean, graphql_name='isMobile')


class SettingsDesktopCheckoutFeatures(sgqlc.types.Type):
    __schema__ = helpling_schema
    date_warning = sgqlc.types.Field(sgqlc.types.list_of('SettingsDesktopCheckoutFeaturesDateWarning'),
                                     graphql_name='dateWarning')
    only_strong_password_allowed = sgqlc.types.Field(Boolean, graphql_name='onlyStrongPasswordAllowed')
    show_agency_card_in_funnel = sgqlc.types.Field(Boolean, graphql_name='showAgencyCardInFunnel')
    show_billing_address_box = sgqlc.types.Field(Boolean, graphql_name='showBillingAddressBox')
    show_cleaner_ironing = sgqlc.types.Field(Boolean, graphql_name='showCleanerIroning')
    show_helpling_shop_link_in_checkout_thank_you = sgqlc.types.Field(Boolean,
                                                                      graphql_name='showHelplingShopLinkInCheckoutThankYou')
    show_unknown_candidates = sgqlc.types.Field(Boolean, graphql_name='showUnknownCandidates')
    show_usp_commitment = sgqlc.types.Field(Boolean, graphql_name='showUspCommitment')
    show_verification_level_badges = sgqlc.types.Field(Boolean, graphql_name='showVerificationLevelBadges')
    sunday_bookings = sgqlc.types.Field(Boolean, graphql_name='sundayBookings')


class SettingsDesktopCheckoutFeaturesDateWarning(sgqlc.types.Type):
    __schema__ = helpling_schema
    day = sgqlc.types.Field(String, graphql_name='day')
    end = sgqlc.types.Field(String, graphql_name='end')
    start = sgqlc.types.Field(String, graphql_name='start')


class SettingsDesktopCheckoutMobileApps(sgqlc.types.Type):
    __schema__ = helpling_schema
    google_store_icon = sgqlc.types.Field(String, graphql_name='googleStoreIcon')
    google_store_link = sgqlc.types.Field(String, graphql_name='googleStoreLink')
    ios_store_icon = sgqlc.types.Field(String, graphql_name='iosStoreIcon')
    ios_store_link = sgqlc.types.Field(String, graphql_name='iosStoreLink')


class SettingsDesktopCheckoutPayments(sgqlc.types.Type):
    __schema__ = helpling_schema
    adyen_public_key = sgqlc.types.Field(String, graphql_name='adyenPublicKey')
    stripe_public_key = sgqlc.types.Field(String, graphql_name='stripePublicKey')


class SettingsDesktopCheckoutType(sgqlc.types.Type):
    __schema__ = helpling_schema
    api = sgqlc.types.Field(SettingsDesktopCheckoutApi, graphql_name='api')
    app_type = sgqlc.types.Field(String, graphql_name='appType')
    bid = sgqlc.types.Field(SettingsDesktopCheckoutBid, graphql_name='bid')
    brand = sgqlc.types.Field(String, graphql_name='brand')
    candidates = sgqlc.types.Field(SettingsDesktopCheckoutCandidates, graphql_name='candidates')
    code = sgqlc.types.Field(String, graphql_name='code')
    components = sgqlc.types.Field(SettingsDesktopCheckoutComponents, graphql_name='components')
    country = sgqlc.types.Field(SettingsDesktopCheckoutCountry, graphql_name='country')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    customer = sgqlc.types.Field(SettingsDesktopCheckoutCustomer, graphql_name='customer')
    device = sgqlc.types.Field(SettingsDesktopCheckoutDevice, graphql_name='device')
    effective_price = sgqlc.types.Field(Int, graphql_name='effectivePrice')
    features = sgqlc.types.Field(SettingsDesktopCheckoutFeatures, graphql_name='features')
    mobile_apps = sgqlc.types.Field(SettingsDesktopCheckoutMobileApps, graphql_name='mobileApps')
    payments = sgqlc.types.Field(SettingsDesktopCheckoutPayments, graphql_name='payments')
    postcode = sgqlc.types.Field(String, graphql_name='postcode')
    provider_types = sgqlc.types.Field(ProviderTypesCategories, graphql_name='providerTypes')
    shared_sprite_path = sgqlc.types.Field(String, graphql_name='sharedSpritePath')
    sprite_path = sgqlc.types.Field(String, graphql_name='spritePath')


class SettingsProviderTypePrices(sgqlc.types.Type):
    __schema__ = helpling_schema
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    max_price = sgqlc.types.Field(String, graphql_name='maxPrice')


class SettingsTimePropType(sgqlc.types.Type):
    __schema__ = helpling_schema
    label = sgqlc.types.Field(String, graphql_name='label')
    title = sgqlc.types.Field(String, graphql_name='title')
    value = sgqlc.types.Field(String, graphql_name='value')


class TaxCertificate(sgqlc.types.Type):
    __schema__ = helpling_schema
    currency_symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currencySymbol')
    customer = sgqlc.types.Field(sgqlc.types.non_null(Customer), graphql_name='customer')
    document_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='documentName')
    document_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='documentPath')
    events_with_transactions_count = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                       graphql_name='eventsWithTransactionsCount')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Provider), graphql_name='provider')
    transactions_total_amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='transactionsTotalAmount')
    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')


class UpdateCurrentUserDetailsError(sgqlc.types.Type):
    __schema__ = helpling_schema
    current_password = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='currentPassword')
    email = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='email')
    first_name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='firstName')
    last_name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lastName')
    mobile = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='mobile')
    password = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='password')
    password_confirmation = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='passwordConfirmation')
    phone = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='phone')


class UpdateMobileError(sgqlc.types.Type):
    __schema__ = helpling_schema
    mobile = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='mobile')


class User(sgqlc.types.Type):
    __schema__ = helpling_schema
    account_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountType')
    firstname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstname')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    preferred_language = sgqlc.types.Field(String, graphql_name='preferredLanguage')


class UserBookingDetailsResultError(sgqlc.types.Type):
    __schema__ = helpling_schema
    instabook_enabled = sgqlc.types.Field(sgqlc.types.list_of(Boolean), graphql_name='instabookEnabled')


class VerticalRequestCandidateType(sgqlc.types.Type):
    __schema__ = helpling_schema
    commission_per_hour = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='commissionPerHour',
                                            args=sgqlc.types.ArgDict((
                                                ('format',
                                                 sgqlc.types.Arg(MoneyFormat, graphql_name='format', default='Plain')),
                                            ))
                                            )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_price_per_hour = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='customerPricePerHour',
                                                args=sgqlc.types.ArgDict((
                                                    ('format', sgqlc.types.Arg(MoneyFormat, graphql_name='format',
                                                                               default='Plain')),
                                                ))
                                                )
    id = sgqlc.types.Field(ID, graphql_name='id')
    opted_in = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='optedIn')
    provider = sgqlc.types.Field(sgqlc.types.non_null(Provider), graphql_name='provider')
    provider_payout_per_hour = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='providerPayoutPerHour',
                                                 args=sgqlc.types.ArgDict((
                                                     ('format', sgqlc.types.Arg(MoneyFormat, graphql_name='format',
                                                                                default='Plain')),
                                                 ))
                                                 )
    provider_total_payout = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='providerTotalPayout',
                                              args=sgqlc.types.ArgDict((
                                                  ('format', sgqlc.types.Arg(MoneyFormat, graphql_name='format',
                                                                             default='Plain')),
                                              ))
                                              )
    request = sgqlc.types.Field(sgqlc.types.non_null('VerticalRequestType'), graphql_name='request')
    service = sgqlc.types.Field(sgqlc.types.non_null(ProviderVerticalServiceType), graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class VerticalRequestType(sgqlc.types.Type):
    __schema__ = helpling_schema
    address = sgqlc.types.Field(Address, graphql_name='address')
    candidates = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(VerticalRequestCandidateType))),
        graphql_name='candidates')
    category = sgqlc.types.Field(String, graphql_name='category')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    current_provider_commission_per_hour = sgqlc.types.Field(Money, graphql_name='currentProviderCommissionPerHour')
    current_provider_customer_price_per_hour = sgqlc.types.Field(Money,
                                                                 graphql_name='currentProviderCustomerPricePerHour')
    current_provider_payout_per_hour = sgqlc.types.Field(Money, graphql_name='currentProviderPayoutPerHour')
    current_provider_total_payout = sgqlc.types.Field(Money, graphql_name='currentProviderTotalPayout')
    customer = sgqlc.types.Field(sgqlc.types.non_null(Customer), graphql_name='customer')
    description = sgqlc.types.Field(String, graphql_name='description')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    endtime = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endtime')
    frequency = sgqlc.types.Field(String, graphql_name='frequency')
    id = sgqlc.types.Field(ID, graphql_name='id')
    opted_in_candidates = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(VerticalRequestCandidateType))),
        graphql_name='optedInCandidates')
    picture_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
                                     graphql_name='pictureUrls')
    postcode = sgqlc.types.Field(String, graphql_name='postcode')
    pricing_unit = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pricingUnit')
    selected_candidates = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(VerticalRequestCandidateType))),
        graphql_name='selectedCandidates')
    starttime = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='starttime')
    unit_quantity = sgqlc.types.Field(Int, graphql_name='unitQuantity')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    winning_candidate = sgqlc.types.Field(VerticalRequestCandidateType, graphql_name='winningCandidate')


class VerticalServiceCategory(sgqlc.types.Type):
    __schema__ = helpling_schema
    config_subcategories = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VerticalsConfigSubcategoryType'))),
        graphql_name='configSubcategories')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pricing_units = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProviderVerticalPricingUnitType))),
        graphql_name='pricingUnits')
    subcategories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
                                      graphql_name='subcategories')


class VerticalsCheckoutSettings(sgqlc.types.Type):
    __schema__ = helpling_schema
    adyen_public_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='adyenPublicKey')
    country = sgqlc.types.Field(sgqlc.types.non_null(CountrySettings), graphql_name='country')
    customer_marketplace_fee = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='customerMarketplaceFee')
    stripe_public_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stripePublicKey')
    vertical_categories = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(VerticalServiceCategory))),
        graphql_name='verticalCategories')


class VerticalsConfigSubcategoryType(sgqlc.types.Type):
    __schema__ = helpling_schema
    date_display = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dateDisplay')
    duration_display = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='durationDisplay')
    fixed_candidate_provider_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)),
                                                     graphql_name='fixedCandidateProviderIds')
    fixed_duration = sgqlc.types.Field(Int, graphql_name='fixedDuration')
    full_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullName')
    funnel_steps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
                                     graphql_name='funnelSteps')
    ignore_availability = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='ignoreAvailability')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pricing_unit = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pricingUnit')
    pricing_unit_display = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pricingUnitDisplay')
    pricing_unit_quantities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)),
                                                graphql_name='pricingUnitQuantities')
    promo_applicable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='promoApplicable')
    show_in_provider_services = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInProviderServices')
    show_in_verticals_checkout = sgqlc.types.Field(sgqlc.types.non_null(Boolean),
                                                   graphql_name='showInVerticalsCheckout')
    skip_pictures = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='skipPictures')
    time_display = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timeDisplay')
    time_slots = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('VerticalsTimeSlot')),
                                   graphql_name='timeSlots')


class VerticalsTimeSlot(sgqlc.types.Type):
    __schema__ = helpling_schema
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    starttime = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='starttime')


class WorkingHour(sgqlc.types.Type):
    __schema__ = helpling_schema
    available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='available')
    close_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='closeTime')
    day = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='day')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    open_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='openTime')
    valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='valid')


class addProvidersToBidPayload(sgqlc.types.Type):
    __schema__ = helpling_schema
    bid = sgqlc.types.Field(CustomerBid, graphql_name='bid')
    errors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ErrorType)), graphql_name='errors')
    providers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
                                  graphql_name='providers')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class bestRatingReceived(sgqlc.types.Type):
    __schema__ = helpling_schema
    comments = sgqlc.types.Field(String, graphql_name='comments')
    rating = sgqlc.types.Field(Float, graphql_name='rating')
    reference = sgqlc.types.Field(Boolean, graphql_name='reference')
    reviewer_name = sgqlc.types.Field(String, graphql_name='reviewerName')


class bidFlexibilities(sgqlc.types.Type):
    __schema__ = helpling_schema
    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class bidPreferences(sgqlc.types.Type):
    __schema__ = helpling_schema
    max_bid_duration = sgqlc.types.Field(Int, graphql_name='maxBidDuration')
    min_bid_duration = sgqlc.types.Field(Int, graphql_name='minBidDuration')


class countryProviderDefaultFilters(sgqlc.types.Type):
    __schema__ = helpling_schema
    ironing = sgqlc.types.Field(Boolean, graphql_name='ironing')
    max_price = sgqlc.types.Field(Int, graphql_name='maxPrice')
    maximum_cleans_filter_value = sgqlc.types.Field(Int, graphql_name='maximumCleansFilterValue')
    min_bookings = sgqlc.types.Field(Int, graphql_name='minBookings')
    min_price = sgqlc.types.Field(Int, graphql_name='minPrice')
    min_rating = sgqlc.types.Field(Int, graphql_name='minRating')
    pets = sgqlc.types.Field(Boolean, graphql_name='pets')


class createCustomerAppRatingError(sgqlc.types.Type):
    __schema__ = helpling_schema
    consent = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='consent')
    reason = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='reason')
    score = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='score')


class createCustomerNewRequestError(sgqlc.types.Type):
    __schema__ = helpling_schema
    frequency = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='frequency')
    promo_code = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='promoCode')
    proposed_duration = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)),
                                          graphql_name='proposedDuration')
    proposed_starttime = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)),
                                           graphql_name='proposedStarttime')
    provider_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='providerId')


class experienceType(sgqlc.types.Type):
    __schema__ = helpling_schema
    experience_description = sgqlc.types.Field(String, graphql_name='experienceDescription')
    experience_headline = sgqlc.types.Field(String, graphql_name='experienceHeadline')
    experience_time_key = sgqlc.types.Field(ExperienceTypeExperienceTimeKeyEnum, graphql_name='experienceTimeKey')


class payloadRecord(sgqlc.types.Type):
    __schema__ = helpling_schema
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class priceRecommendations(sgqlc.types.Type):
    __schema__ = helpling_schema
    one_off_max_price = sgqlc.types.Field(Int, graphql_name='oneOffMaxPrice')
    one_off_min_price = sgqlc.types.Field(Int, graphql_name='oneOffMinPrice')
    recurring_max_price = sgqlc.types.Field(Int, graphql_name='recurringMaxPrice')
    recurring_min_price = sgqlc.types.Field(Int, graphql_name='recurringMinPrice')


class prices(sgqlc.types.Type):
    __schema__ = helpling_schema
    customer_one_off_price = sgqlc.types.Field(Int, graphql_name='customerOneOffPrice')
    customer_recurring_price = sgqlc.types.Field(Int, graphql_name='customerRecurringPrice')
    one_off_commission_per_hour = sgqlc.types.Field(Float, graphql_name='oneOffCommissionPerHour')
    one_off_payout_per_hour = sgqlc.types.Field(Float, graphql_name='oneOffPayoutPerHour')
    one_off_price = sgqlc.types.Field(Int, graphql_name='oneOffPrice')
    recurring_commission_per_hour = sgqlc.types.Field(Float, graphql_name='recurringCommissionPerHour')
    recurring_payout_per_hour = sgqlc.types.Field(Float, graphql_name='recurringPayoutPerHour')
    recurring_price = sgqlc.types.Field(Int, graphql_name='recurringPrice')


class reactivateProviderResult(sgqlc.types.Type):
    __schema__ = helpling_schema
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    work_status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workStatus')


class settings(sgqlc.types.Type):
    __schema__ = helpling_schema
    desktop_checkout = sgqlc.types.Field(SettingsDesktopCheckoutType, graphql_name='desktopCheckout',
                                         args=sgqlc.types.ArgDict((
                                             ('bid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='bid',
                                                                     default=None)),
                                         ))
                                         )
    verticals_checkout = sgqlc.types.Field(VerticalsCheckoutSettings, graphql_name='verticalsCheckout')


class updateProfileBidDurationResultErrorRange(sgqlc.types.Type):
    __schema__ = helpling_schema
    max_bid_duration = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='maxBidDuration')
    min_bid_duration = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='minBidDuration')


class updateProfileResultError(sgqlc.types.Type):
    __schema__ = helpling_schema
    experience_description = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='experienceDescription')
    experience_headline = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='experienceHeadline')
    picture = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='picture')
    tax_id = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='taxId')
    vat_id = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='vatId')


class CurrentUserType(sgqlc.types.Type, CurrentUserInterface):
    __schema__ = helpling_schema
    account_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountType')
    address = sgqlc.types.Field(Address, graphql_name='address')
    chat_terms_agreed_on = sgqlc.types.Field(DateTime, graphql_name='chatTermsAgreedOn')
    firstname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstname')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    preferred_language = sgqlc.types.Field(String, graphql_name='preferredLanguage')


class CustomerCurrentUserType(sgqlc.types.Type, CurrentUserInterface):
    __schema__ = helpling_schema
    ab_tests = sgqlc.types.Field(CustomerAbTestsType, graphql_name='abTests')
    account_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountType')
    address = sgqlc.types.Field(Address, graphql_name='address')
    chat_terms_agreed_on = sgqlc.types.Field(DateTime, graphql_name='chatTermsAgreedOn')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    firstname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='firstname')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    last_app_rating_at = sgqlc.types.Field(DateTime, graphql_name='lastAppRatingAt')
    lastname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastname')
    mobile = sgqlc.types.Field(String, graphql_name='mobile')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    preferred_language = sgqlc.types.Field(String, graphql_name='preferredLanguage')
    referral_code = sgqlc.types.Field(Promo, graphql_name='referralCode')
    requires_payment_details = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresPaymentDetails')


class CustomerRating(sgqlc.types.Type, Rating):
    __schema__ = helpling_schema
    comments = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='comments')
    communication = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='communication')
    customer = sgqlc.types.Field(Customer, graphql_name='customer')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    quality = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='quality')
    read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='read')
    reliability = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='reliability')
    total = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='total', args=sgqlc.types.ArgDict((
        ('precision', sgqlc.types.Arg(Int, graphql_name='precision', default=None)),
    ))
                              )


class ProviderAvgRating(sgqlc.types.Type, Rating):
    __schema__ = helpling_schema
    communication = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='communication')
    quality = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='quality')
    reliability = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='reliability')
    total = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='total')


class ProviderRating(sgqlc.types.Type, Rating):
    __schema__ = helpling_schema
    comment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='comment')
    communication = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='communication')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createdAt')
    created_at_formatted = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createdAtFormatted')
    customer = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customer')
    customer_short_full_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customerShortFullName')
    customer_shortname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customerShortname')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    quality = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='quality')
    read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='read')
    reference = sgqlc.types.Field(Boolean, graphql_name='reference')
    reliability = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='reliability')
    reviewer_name = sgqlc.types.Field(String, graphql_name='reviewerName')
    total = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='total', args=sgqlc.types.ArgDict((
        ('precision', sgqlc.types.Arg(Int, graphql_name='precision', default=None)),
    ))
                              )


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
helpling_schema.query_type = Query
helpling_schema.mutation_type = Mutation
helpling_schema.subscription_type = None
