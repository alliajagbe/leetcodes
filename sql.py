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
# Replace Employee ID with the Unique Identifier
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

#%%
'''
# Product Sales Analysis I
Write a solution to report the product_name, year, 
and price for each sale_id in the Sales table.

Return the resulting table in any order.
'''
sql = '''
        select p.product_name, s.year, s.price
        from Sales s inner join Product p
        where s.product_id = p.product_id
        '''

#%%
'''
# Customers Who Visited But Did Not Make Any Transactions
Write a solution to find the IDs of the users who visited
without making any transactions and the number of times 
they made these types of visits.

Return the result table sorted in any order.
'''
sql = '''
        select v.customer_id, count(v.visit_id) as count_no_trans 
        from Visits v 
        left join Transactions t 
        on v.visit_id = t.visit_id 
        where t.transaction_id is NULL 
        group by v.customer_id
        '''

#%% 
'''
# Rising Temperature
Find all dates' Id with higher temperatures compared to 
its previous dates (yesterday).

Return the result table in any order.
'''
sql = '''
        select x.id from Weather x
        join Weather y
        on datediff(x.recordDate, y.recordDate) = 1
        and x.Temperature > y.Temperature
        '''

#%%
'''
# Average Time of Process per Machine
There is a factory website that has several machines each 
running the same number of processes. 
Write a solution to find the average time each machine 
takes to complete a process.

The time to complete a process is the 'end' timestamp 
minus the 'start' timestamp. 
The average time is calculated by the total time to complete 
every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id 
along with the average time as processing_time, 
which should be rounded to 3 decimal places.

Return the result table in any order.
'''