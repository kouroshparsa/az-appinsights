az-sights
==========

This is a package can be used to query Azure Application Insights.
Other packages currently fail to login with the error:
```
AttributeError: 'DefaultAzureCredential' object has no attribute 'signed_session'
```

# Installation

First install Azure CLI: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

Then, in the terminal run:
`az login`

How to install:

`pip install az_sights`


```python
import az_sights

if __name__ == '__main__':
    res = az_sights.query_today('app_id', 'some query')
    res = az_sights.query_this_month('app_id', 'some query')
```

You query must be a valid KQL query like:

```customEvents | where  name == 'click'```

If you want to query in a specific date range:
```python
import az_sights

if __name__ == '__main__':
    start_date = '2012-01-15'
    end_date = '2012-03-15'
    res = az_sights.query_app_insights('app_id', 'some query', start_date, end_date)
```

Note that the first time you run this, it will check whether you have the `application-insights` extension installed. If you do not, it will try to install it for you.
