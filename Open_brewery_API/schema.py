brewery_schema = {
        "type": "object",
        "required": [
            "id",
            "name",
            "brewery_type",
            "address_1",
            "address_2",
            "address_3",
            "city",
            "state_province",
            "postal_code",
            "country",
            "longitude",
            "latitude",
            "phone",
            "website_url",
            "state",
            "street"
        ],
        "properties": {
            "id": {
                "type": "string",
                "pattern": "^.*$"
            },
            "name": {
                "type": "string",
                "pattern": "^.*$"
            },
            "brewery_type": {
                "type": "string"
            },
            "address_1": {
                "type": "string"
            },
            "address_2": {
                "type": "null"
            },
            "address_3": {
                "type": "null"
            },
            "city": {
                "type": "string"
            },
            "state_province": {
                "type": "string"
            },
            "postal_code": {
                "type": "string"
            },
            "country": {
                "type": "string"
            },
            "longitude": {
                "type": "string"
            },
            "latitude": {
                "type": "string"
            },
            "phone": {
                "type": "string"
            },
            "website_url": {
                "type": "string"
            },
            "state": {
                "type": "string"
            },
            "street": {
                "type": "string"
            }
        }
    }


