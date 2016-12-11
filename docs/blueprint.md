FORMAT: 1A
HOST: http://localhost:8000/

# Channels API
The channels api provides the functionality to retrieve any channel and it's associated categories.

## Group Channel

Resources related to channels.

## Channel Collection [/channels/]

### List All Questions [GET]

+ Response 200 (application/json)
    + Body

            [
                {
                    "uuid":"4991a3f3-d9b5-4b2e-9828-5f08eab6c298",
                    "name":"testchannel"
                },
                {
                    "uuid": "6823618-921f-4c60-ab5c-97c3e1097bcf",
                    "name":"anotherchannel"
                }
            ]

## Single Channel [/channels/{name}/]

+ Parameters
    + name: `testchannel` (string, required) - Name of an existing channel

### Retrieve a single channel [GET]
Retrieve a single channel with its categories.

+ Response 200 (application/json)
    + Body

            {
                "uuid": "4991a3f3-d9b5-4b2e-9828-5f08eab6c298",
                "name": "testchannel",
                "categories": [
                    {
                        "uuid": "645df43d-95bf-4469-b9e4-b91e7996ad6b",
                        "name": "Computers",
                        "children": [
                            {
                                "uuid": "c856f358-fcb9-431f-8fb4-4f57e7430e39",
                                "name": "Desktop",
                                "children": []
                            },
                            {
                                "uuid": "940ddd0f-bdd6-4da2-9eb8-682a6db3c225",
                                "name": "Notebooks",
                                "children": []
                            },
                            {
                                "uuid": "d0fb8139-ac3e-4983-8db9-195889f269a9",
                                "name": "Tablets",
                                "children": []
                            }
                        ]
                    },
                    {
                        "uuid": "c7e1894d-99e6-437b-a46b-4d39e924644f",
                        "name": "Games",
                        "children": [
                            {
                                "uuid": "bd699f68-2539-4463-94c3-123838a354a7",
                                "name": "XBOX One",
                                "children": [
                                    {
                                        "uuid": "83f973d8-9528-4102-ab26-fcdf4ce2ab7c",
                                        "name": "Games",
                                        "children": []
                                    },
                                    {
                                        "uuid": "ae582dc9-75e8-4471-af34-b5377a210e88",
                                        "name": "Accessories",
                                        "children": []
                                    },
                                    {
                                        "uuid": "bfa42491-8d6e-4534-95ca-cade0ef3b50f",
                                        "name": "Console",
                                        "children": []
                                    }
                                ]
                            },
                            {
                                "uuid": "cf9f7c45-da1b-4524-9659-0c58f97b9dd8",
                                "name": "XBOX 360",
                                "children": [
                                    {
                                        "uuid": "b0ff0595-5fe5-4a37-b538-7e0fa1ff68a0",
                                        "name": "Games",
                                        "children": []
                                    },
                                    {
                                        "uuid": "6c3c53b0-bd50-4cb2-8494-62a1514acb9d",
                                        "name": "Accessories",
                                        "children": []
                                    },
                                    {
                                        "uuid": "d5ac0f34-4473-4849-8ffb-0547b4932a82",
                                        "name": "Console",
                                        "children": []
                                    }
                                ]
                            },
                            {
                                "uuid": "34759555-a913-435d-ac88-c7f263e34d5c",
                                "name": "Playstation 4",
                                "children": []
                            }
                        ]
                    },
                    {
                        "uuid": "125d6ec0-4c05-4924-9b94-25b3cc308876",
                        "name": "Books",
                        "children": [
                            {
                                "uuid": "41932d55-2c88-41da-9efa-acdcb3adc68d",
                                "name": "Computers",
                                "children": [
                                    {
                                        "uuid": "c492afc9-b247-4035-a636-a7955eac7eba",
                                        "name": "Programming",
                                        "children": []
                                    },
                                    {
                                        "uuid": "f3329d05-c181-4356-bda3-fabb9c5ea30e",
                                        "name": "Database",
                                        "children": []
                                    },
                                    {
                                        "uuid": "d56fbb3d-55d4-472f-907a-6c447f02988d",
                                        "name": "Applications",
                                        "children": []
                                    }
                                ]
                            },
                            {
                                "uuid": "86f4e134-ad9d-43cd-9638-57b5eb562a56",
                                "name": "Foreign Literature",
                                "children": []
                            },
                            {
                                "uuid": "d7a77603-881e-429e-a7dd-c797ee4a01a4",
                                "name": "National Literature",
                                "children": [
                                    {
                                        "uuid": "ccaef8b7-fbc5-462d-9378-b635fa611cc3",
                                        "name": "Fiction Fantastic",
                                        "children": []
                                    },
                                    {
                                        "uuid": "abd5a175-21d5-4ff5-90d7-29fd86d60454",
                                        "name": "Science Fiction",
                                        "children": []
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }

## Group Category

Resources related to categories.

## Single Category [/category/{uuid}/]

+ Parameters
    + uuid: `41932d55-2c88-41da-9efa-acdcb3adc68d` - (string, required) Name of an existing category

### Retrieve a single category [GET]

Retrieve a single category along with its parents and children.

+ Response 200 (application/json)
    + Body
    
            {
                "uuid": "41932d55-2c88-41da-9efa-acdcb3adc68d",
                "name": "Computers",
                "children": [
                    {
                        "uuid": "c492afc9-b247-4035-a636-a7955eac7eba",
                        "name": "Programming",
                        "children": []
                    },
                    {
                        "uuid": "f3329d05-c181-4356-bda3-fabb9c5ea30e",
                        "name": "Database",
                        "children": []
                    },
                    {
                        "uuid": "d56fbb3d-55d4-472f-907a-6c447f02988d",
                        "name": "Applications",
                        "children": []
                    }
                ],
                "parent": {
                    "uuid": "125d6ec0-4c05-4924-9b94-25b3cc308876",
                    "name": "Books",
                    "parent": null
                }
            }
