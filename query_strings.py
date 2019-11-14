fetch_candidates = """
query fetchPotentialCandidatesForBid($bidCode: String!, $minPrice: Int!, $maxPrice: Int!, $minRating: Int!, $minBookings: Int!, $pets: Boolean!, $ironing: Boolean!, $endCursor: String!, $sort: CustomerBidPotentialCandidateOrderFields!) {
  customerBid(code: $bidCode) {
    potentialCandidates(first: 1000, minPrice: $minPrice, maxPrice: $maxPrice, minRating: $minRating, minBookings: $minBookings, pets: $pets, ironing: $ironing, after: $endCursor, sort: $sort) {
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      totalCount
      maximumPriceFilter
      minimumPriceFilter
      edges {
        node {
          provider {
            id
            firstname
            shortname
            defaultProfileImage
            avgRating(precision: 1) {
              total
              __typename
            }
            pets
            windows
            ironing
            ratingsReceivedCount
            verificationLevel
            documents
            performedCleaningsCount
            experience {
              experienceHeadline
              experienceDescription
              experienceTimeKey
              __typename
            }
            languageSkills
            instabookEnabled
            __typename
          }
          pricePerHour
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}"""

query = """query fetchCheckoutDesktopSettings($bidId: String!) {
  settings {
    desktopCheckout(bid: $bidId) {
      code
      postcode
      effectivePrice
      currency
      components {
        frequency {
          props {
            recurringPrice
            oneOffPrice
            recurringInt
            onceOffInt
            repeatDiscount
            __typename
          }
          default
          __typename
        }
        duration {
          props {
            oneOff {
              hiddenOptions {
                label
                value
                __typename
              }
              visibleOptions {
                label
                value
                __typename
              }
              __typename
            }
            recurring {
              hiddenOptions {
                label
                value
                __typename
              }
              visibleOptions {
                label
                value
                __typename
              }
              __typename
            }
            __typename
          }
          default {
            oneOff {
              label
              value
              __typename
            }
            recurring {
              label
              value
              __typename
            }
            __typename
          }
          __typename
        }
        date {
          props {
            defaultDay
            disabledDays
            __typename
          }
          default
          __typename
        }
        time {
          props {
            options {
              value
              title
              __typename
            }
            __typename
          }
          default {
            value
            title
            __typename
          }
          __typename
        }
        extras {
          props {
            items {
              badge
              label
              name
              priceOneOff
              priceRecurring
              time
              __typename
            }
            __typename
          }
          default
          __typename
        }
        payments {
          props {
            methods
            __typename
          }
          __typename
        }
        __typename
      }
      bid {
        identifier
        promo {
          code
          value
          active
          oneOff
          repeat
          minHours
          onlyNewCustomer
          valueType
          services
          startsAt
          expiresAt
          maxUsageCount
          usageCount
          __typename
        }
        frequency
        duration {
          label
          value
          __typename
        }
        date
        time {
          label
          title
          value
          __typename
        }
        replacementForType
        addressId
        __typename
      }
      features {
        dateWarning {
          day
          start
          end
          __typename
        }
        showAgencyCardInFunnel
        showBillingAddressBox
        onlyStrongPasswordAllowed
        showUnknownCandidates
        showCleanerIroning
        showVerificationLevelBadges
        showHelplingShopLinkInCheckoutThankYou
        showUspCommitment
        sundayBookings
        __typename
      }
      candidates {
        data {
          id
          userId
          selected
          firstname
          lastname
          shortname
          profileImage
          averageRating
          pets
          windows
          laundry
          ironing
          ratingsReceivedCount
          activeRelationshipsCount
          goliveDate
          performedCleaningsCount
          gender
          picture
          averageRatingFloat
          pricePerHour
          verificationLevel
          documents
          languageSkills
          experienceHeadline
          experienceDescription
          topValue
          performanceScore
          bestRatingReceived {
            reviewerName
            comments
            rating
            reference
            __typename
          }
          __typename
        }
        __typename
      }
      providerTypes {
        topRated {
          adhoc {
            maxPrice
            enabled
            __typename
          }
          repeat {
            maxPrice
            enabled
            __typename
          }
          __typename
        }
        agency {
          adhoc {
            maxPrice
            enabled
            __typename
          }
          repeat {
            maxPrice
            enabled
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}
"""

transition_to_provider_selection = """
mutation transitionBidToProviderSelection($bidCode: String!, $repeat: Boolean!, $frequency: Frequency!, $duration: Int!, $date: String!, $time: String!, $ironing: Boolean!, $pets: Boolean!, $materialsRequired: Boolean!, $workdayFlexibility: Boolean!, $providerType: String!, $notes: String!) {
  transitionBidToProviderSelection(bidCode: $bidCode, frequency: $frequency, repeat: $repeat, duration: $duration, date: $date, time: $time, ironing: $ironing, pets: $pets, materialsRequired: $materialsRequired, workdayFlexibility: $workdayFlexibility, providerType: $providerType, notes: $notes) {
    success
    errors {
      message
      __typename
    }
    __typename
  }
}
"""
