"""
Assignment 5 Success Example: List or Dictionary Mini-App

This example creates a small campus resource lookup tool using a dictionary.
"""


campus_resources = {
    "tutoring": {
        "location": "Learning Center",
        "contact": "tutoring@example.edu",
        "available": True,
    },
    "library": {
        "location": "Main Building",
        "contact": "library@example.edu",
        "available": True,
    },
    "career": {
        "location": "Student Services",
        "contact": "career@example.edu",
        "available": False,
    },
}

requested_resource = "tutoring"

print("Available campus resources:")

for resource_name in campus_resources:
    print("-", resource_name)

print("\nLookup result:")

if requested_resource in campus_resources:
    resource = campus_resources[requested_resource]

    print("Resource:", requested_resource)
    print("Location:", resource["location"])
    print("Contact:", resource["contact"])

    if resource["available"]:
        print("Status: available")
    else:
        print("Status: not currently available")
else:
    print("Resource not found:", requested_resource)

