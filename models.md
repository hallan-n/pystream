login
    id
    email
    password
    created_at
profiles
    id
    login_id
    name
    icon
    created_at

    create_profile - Ok
    update_profile
    get_all_profiles
    get_profile
    delete_profiles


plans
    id
    name
    max_profiles
    login_id



catalog
    id
    login_plans_id
    name
    description
series
    id
    catalog_id
    title
    seasons
films
    id
    catalog_id
    title
    duration
episodes
    id
    series_id
    title
    episode
    seasion
    duration
categories
    id
    episode_id
    name
    description