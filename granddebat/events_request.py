import json
initial_request = """query EventPageQuery($cursor: String, $count: Int, $search: String, $theme: ID, $project: ID, $isFuture: Boolean) {
  ...EventPageHeader_query_a9h1O
  ...EventRefetch_query_a9h1O
}

fragment EventPageHeader_query_a9h1O on Query {
  events(first: $count, after: $cursor, theme: $theme, project: $project, search: $search, isFuture: $isFuture) {
    totalCount
  }
}

fragment EventRefetch_query_a9h1O on Query {
  ...EventListPaginated_query_a9h1O
  ...EventPageHeader_query_a9h1O
}

fragment EventListPaginated_query_a9h1O on Query {
  events(first: $count, after: $cursor, theme: $theme, project: $project, search: $search, isFuture: $isFuture) {
    totalCount
    ...EventMap_events
    edges {
      node  {
        id
        ...EventPreview_event
        __typename
      }
      cursor
    }
    pageInfo {
      hasPreviousPage
      hasNextPage
      startCursor
      endCursor
    }
  }
}

fragment EventMap_events on EventConnection {
  totalCount
  edges {
    node {
      id
      lat
      lng
      url
      address
      startAt
      endAt
      title
    }
  }
}

fragment EventPreview_event on Event {
  id
  startAt
  endAt
  createdAt
  body
  link
  enabled
  comments {
    totalCount
  }
  title
  fullAddress
  city
  zipCode
  url
  
  themes {
    id
    title
    url
  }
  participants {
    totalCount
  }
  author {
    userType {
      id
      name
    }
    vip
    #zipCode
		#createdAt
    id
    displayName
    username
    isEmailConfirmed
    opinionsCount
    argumentsCount
    projectsCount
    proposalsCount
    votes {
      totalCount
    }
    events {
      totalCount
    }
  }
}"""
# initial_payload = """{\"query\":\"query EventPageQuery($cursor: String, $count: Int, $search: String, $theme: ID, $project: ID, $isFuture: Boolean) {\\n  ...EventPageHeader_query_a9h1O\\n  ...EventRefetch_query_a9h1O\\n}\\n\\nfragment EventPageHeader_query_a9h1O on Query {\\n  events(first: $count, after: $cursor, theme: $theme, project: $project, search: $search, isFuture: $isFuture) {\\n    totalCount\\n  }\\n}\\n\\nfragment EventRefetch_query_a9h1O on Query {\\n  ...EventListPaginated_query_a9h1O\\n  ...EventPageHeader_query_a9h1O\\n}\\n\\nfragment EventListPaginated_query_a9h1O on Query {\\n  events(first: $count, after: $cursor, theme: $theme, project: $project, search: $search, isFuture: $isFuture) {\\n    totalCount\\n    ...EventMap_events\\n    edges {\\n      node  {\\n        id\\n        ...EventPreview_event\\n        __typename\\n      }\\n      cursor\\n    }\\n    pageInfo {\\n      hasPreviousPage\\n      hasNextPage\\n      startCursor\\n      endCursor\\n    }\\n  }\\n}\\n\\nfragment EventMap_events on EventConnection {\\n  totalCount\\n  edges {\\n    node {\\n      id\\n      lat\\n      lng\\n      url\\n      address\\n      startAt\\n      endAt\\n      title\\n    }\\n  }\\n}\\n\\nfragment EventPreview_event on Event {\\n  id\\n  startAt\\n  endAt\\n  createdAt\\n  body\\n  link\\n  enabled\\n  comments {\\n    totalCount\\n  }\\n  title\\n  fullAddress\\n  city\\n  zipCode\\n  url\\n  \\n  themes {\\n    id\\n    title\\n    url\\n  }\\n  participants {\\n    totalCount\\n  }\\n  author {\\n    userType {\\n      id\\n      name\\n    }\\n    vip\\n    #zipCode\\n\\t\\t#createdAt\\n    id\\n    isEmailConfirmed\\n    opinionsCount\\n    argumentsCount\\n    projectsCount\\n    proposalsCount\\n    votes {\\n      totalCount\\n    }\\n    events {\\n      totalCount\\n    }\\n  }\\n}\\n\",\n \"variables\": {\"cursor\":null, \"count\": 100, \"theme\": null, \"project\": null, \"search\": null,\n                   \"isFuture\": true}}"""
initial_payload = {'query': initial_request, "variables": {"cursor":None, "count": 100, "theme": None, "project": None, "search": None, "isFuture": True}}
initial_payload = json.dumps(initial_payload)
initial_payload = initial_payload.replace('\n', '\\n')
paginated_request = """
query EventListPaginatedQuery($cursor: String, $count: Int, $theme: ID, $project: ID, $search: String, $isFuture: Boolean) {
  ...EventListPaginated_query_a9h1O
}

fragment EventListPaginated_query_a9h1O on Query {
  events(first: $count, after: $cursor, theme: $theme, project: $project, search: $search, isFuture: $isFuture) {
    totalCount
    ...EventMap_events
    edges {
      node {
        id
        ...EventPreview_event
        __typename
      }
      cursor
    }
    pageInfo {
      hasPreviousPage
      hasNextPage
      startCursor
      endCursor
    }
  }
}

fragment EventMap_events on EventConnection {
  totalCount
  edges {
    node {
      id
      lat
      lng
      url
      address
      startAt
      endAt
      title
    }
  }
}

fragment EventPreview_event on Event {
  id
  startAt
  endAt
  createdAt
  body
  link
  enabled
  comments {
    totalCount
  }
  title
  fullAddress
  city
  zipCode
  url
  
  themes {
    id
    title
    url
  }
  participants {
    totalCount
  }
  author {
    userType {
      id
      name
    }
    vip
    id
    displayName
    username
    isEmailConfirmed
    opinionsCount
    argumentsCount
    projectsCount
    proposalsCount
    votes {
      totalCount
    }
    events {
      totalCount
    }
  }
}
"""
# paginated_payload = """{\"query\":\"query EventListPaginatedQuery($cursor: String, $count: Int, $theme: ID, $project: ID, $search: String, $isFuture: Boolean) {\\n  ...EventListPaginated_query_a9h1O\\n}\\n\\nfragment EventListPaginated_query_a9h1O on Query {\\n  events(first: $count, after: $cursor, theme: $theme, project: $project, search: $search, isFuture: $isFuture) {\\n    totalCount\\n    ...EventMap_events\\n    edges {\\n      node {\\n        id\\n        ...EventPreview_event\\n        __typename\\n      }\\n      cursor\\n    }\\n    pageInfo {\\n      hasPreviousPage\\n      hasNextPage\\n      startCursor\\n      endCursor\\n    }\\n  }\\n}\\n\\nfragment EventMap_events on EventConnection {\\n  totalCount\\n  edges {\\n    node {\\n      id\\n      lat\\n      lng\\n      url\\n      address\\n      startAt\\n      endAt\\n      title\\n    }\\n  }\\n}\\n\\nfragment EventPreview_event on Event {\\n  id\\n  startAt\\n  endAt\\n  createdAt\\n  body\\n  link\\n  enabled\\n  comments {\\n    totalCount\\n  }\\n  title\\n  fullAddress\\n  city\\n  zipCode\\n  url\\n  \\n  themes {\\n    id\\n    title\\n    url\\n  }\\n  participants {\\n    totalCount\\n  }\\n  author {\\n    userType {\\n      id\\n      name\\n    }\\n    vip\\n    #zipCode\\n\\t\\t#createdAt\\n    id\\n    isEmailConfirmed\\n    opinionsCount\\n    argumentsCount\\n    projectsCount\\n    proposalsCount\\n    votes {\\n      totalCount\\n    }\\n    events {\\n      totalCount\\n    }\\n  }\\n}\\n\",\"operationName\":\"EventListPaginatedQuery\",\"variables\": {\"cursor\":\"cursor_replace\", \"count\": 100, \"theme\": null, \"project\": null, \"search\": null,\"isFuture\": true}}"""
paginated_request = paginated_request.replace('\\n', '\\\\n')
paginated_payload = {'query': paginated_request, "variables": {"cursor":"cursor_replace", "count": 100, "theme": None, "project": None, "search": None, "isFuture": True, "userType": None}}
paginated_payload = json.dumps(paginated_payload)
# paginated_payload = paginated_payload.replace('"', '\\"')
