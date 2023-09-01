'''
# Recyclable and Low Fat Products
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') 
where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') 
where 'Y' means this product is recyclable and 'N' means it is not.
'''
sql = """select product_id 
        from Products 
        where low_fats = 'Y' 
            and recyclable = 'Y'
        """

#%%
'''
# Find Customer Referee
Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.
'''

sql = """
        select name 
        from Customer 
        where coalesce(referee_id,0) <> 2;
        """

sql2 = """
        select name 
        from Customer 
        where (referee_id != 2) 
            or (referee_id is NULL);
        """

#%%

''''
# Big Countries
A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.
'''

sql = """
        select name, population, area 
        from World 
        where area >= 3000000 
            or population >= 25000000
            """

#%%
'''
# Article Views I
Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.
'''
sql = """
        select distinct author_id as id
        from Views
        where author_id = viewer_id
        order by author_id
        """

#%%
'''
# Invalid Tweets
Write a solution to find the IDs of the invalid tweets. 
The tweet is invalid if the number of characters used in the content of 
the tweet is strictly greater than 15.

Return the result table in any order.
'''
sql = """
        select tweet_id from Tweets where length(content) > 15
        """

#%%
'''
Write a solution to show the unique ID of each user, 
If a user does not have a unique ID replace just show null.

Return the result table in any order.
'''
sql = '''
        select u.unique_id, e.name
        from Employees e
        left join EmployeeUNI u
        on e.id = u.id
        '''