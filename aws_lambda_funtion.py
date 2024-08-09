import json,re,boto3


####### twitter post tablename = twitter_post     key twitter_post
####### twitter hastag table name = twitter_hashtag key   treanding_tag

def treanding_hashtag_data():
    boto_client = boto3.client('dynamodb',region_name = "us-east-1")
   
    scan_param = {'TableName':'twitter_hashtag'}
    res= boto_client.scan(**scan_param)
    trending_tags = {item['treanding_tag']['S']:item['count_tag']['N'] for item in res["Items"]}
    return trending_tags


def lambda_handler(event, context):
    
    

    data = json.loads(event['body'])
    if data["type"] == "Post":
    
        twitter_post = data["post"]
        hashtags = re.findall(r'#(\w+)', twitter_post)
        post_content = twitter_post
        dynamodb = boto3.resource('dynamodb',region_name= "us-east-1") 

        table_post = dynamodb.Table('twitter_post') 
        # #inserting values into table 
        response = table_post.put_item( 
        Item={'twitter_post': post_content })
                
        hashtag_dict = treanding_hashtag_data()

        table_hashtag = dynamodb.Table('twitter_hashtag') 

        for i in hashtags:
            i = i.lower()
            
            if i in hashtag_dict: 
                hashtag_value = hashtag_dict[i]
                try:
                    hashtag_value = int(hashtag_value)
                except Exception:
                    pass
                hashtag_value += 1
                resp = table_hashtag.update_item(
                    Key={'treanding_tag': i},
                    UpdateExpression="SET count_tag= :n",
                    ExpressionAttributeValues={':n': hashtag_value},
                    ReturnValues="UPDATED_NEW"
                )
            else:
                resp = table_hashtag.put_item( 
                Item={'treanding_tag': i,'count_tag':1 })
                

        
                
        
        return {
            'statusCode': 200,
            'body': json.dumps({"res":"Tweet is posted"})
        }


    elif data["type"]=="Trending Hashtag":
        boto_client = boto3.client('dynamodb',region_name = "us-east-1")
   
        scan_param = {'TableName':'twitter_hashtag'}
        res= boto_client.scan(**scan_param)


        trending_tags = {item['treanding_tag']['S']:item['count_tag']['N'] for item in res["Items"]}
        
        return {
            'statusCode': 200,
            'body': json.dumps(trending_tags)
        }




