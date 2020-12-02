import numpy as np

from recommendation_engines import SoftmaxRecommender


areas_mapper = {
    0: 'Action',
    1: 'Comedy',
    2: 'Horror',
    3: 'Drama',
    4: 'Thriller'
}

products_mapper = {
    'Action': {
        0: 'Indiana Jones',
        1: 'Terminator',
        2: 'The Matrix'
    },

    'Comedy': {
        0: 'Scary Movie',
        1: 'Borat',
        2: 'Hot Fuzz'
    },

    'Horror': {
        0: 'The Evil Dead',
        1: 'The Thing',
        2: 'They Live'
    },

    'Drama': {
        0: 'Bicycle Thieves',
        1: 'Patch Adams',
        2: 'Awakenings'
    },

    'Thriller': {
        0: 'Zodiac',
        1: 'Silence of the Lamb',
        2: 'Shutter Island'
    }

}

areas_dict = {
    customer_id: np.random.randint(0, 100, size=5) for
    customer_id in range(100000)
}
products_dict = {
    area_id: np.random.randint(0, 100, size=(3)) for area_id in range(5)
}


recommender = SoftmaxRecommender(
    areas_dict=areas_dict,
    products_dict=products_dict,
    areas_mapper=areas_mapper,
    products_mapper=products_mapper
)

for user_id in np.random.randint(0, 100000, 15):

    area, product = recommender.recommend(
        query_id=user_id,
        temperature_area=40,
        temperature_product=40
    )
    print(f'User {user_id} might like a {area} movie like {product}')
