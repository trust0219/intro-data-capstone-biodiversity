{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone 2: Biodiversity Project"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "You are a biodiversity analyst working for the National Parks Service.  You're going to help them analyze some data about species at various national parks.\n",
    "\n",
    "Note: The data that you'll be working with for this project is *inspired* by real data, but is mostly fictional."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 1\n",
    "Import the modules that you'll be using in this assignment:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 2\n",
    "You have been given two CSV files. `species_info.csv` with data about different species in our National Parks, including:\n",
    "- The scientific name of each species\n",
    "- The common names of each species\n",
    "- The species conservation status\n",
    "\n",
    "Load the dataset and inspect it:\n",
    "- Load `species_info.csv` into a DataFrame called `species`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "species = pd.read_csv('species_info.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Inspect each DataFrame using `.head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Clethrionomys gapperi gapperi</td>\n",
       "      <td>Gapper's Red-Backed Vole</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos bison</td>\n",
       "      <td>American Bison, Bison</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos taurus</td>\n",
       "      <td>Aurochs, Aurochs, Domestic Cattle (Feral), Dom...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Cervus elaphus</td>\n",
       "      <td>Wapiti Or Elk</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  category                scientific_name  \\\n",
       "0   Mammal  Clethrionomys gapperi gapperi   \n",
       "1   Mammal                      Bos bison   \n",
       "2   Mammal                     Bos taurus   \n",
       "3   Mammal                     Ovis aries   \n",
       "4   Mammal                 Cervus elaphus   \n",
       "\n",
       "                                        common_names conservation_status  \n",
       "0                           Gapper's Red-Backed Vole                 NaN  \n",
       "1                              American Bison, Bison                 NaN  \n",
       "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...                 NaN  \n",
       "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)                 NaN  \n",
       "4                                      Wapiti Or Elk                 NaN  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 3\n",
    "Let's start by learning a bit more about our data.  Answer each of the following questions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many different species are in the `species` DataFrame?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5541"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.scientific_name.nunique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `category` in `species`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Mammal', 'Bird', 'Reptile', 'Amphibian', 'Fish', 'Vascular Plant',\n",
       "       'Nonvascular Plant'], dtype=object)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.category.unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `conservation_status`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([nan, 'Species of Concern', 'Endangered', 'Threatened', 'In Recovery'], dtype=object)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.conservation_status.unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Let's start doing some analysis!\n",
    "\n",
    "The column `conservation_status` has several possible values:\n",
    "- `Species of Concern`: declining or appear to be in need of conservation\n",
    "- `Threatened`: vulnerable to endangerment in the near future\n",
    "- `Endangered`: seriously at risk of extinction\n",
    "- `In Recovery`: formerly `Endangered`, but currnetly neither in danger of extinction throughout all or a significant portion of its range\n",
    "\n",
    "We'd like to count up how many species meet each of these criteria.  Use `groupby` to count how many `scientific_name` meet each of these criteria."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>scientific_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Endangered</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>In Recovery</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>151</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Threatened</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  conservation_status  scientific_name\n",
       "0          Endangered               15\n",
       "1         In Recovery                4\n",
       "2  Species of Concern              151\n",
       "3          Threatened               10"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.groupby('conservation_status').scientific_name.nunique().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we saw before, there are far more than 200 species in the `species` table.  Clearly, only a small number of them are categorized as needing some sort of protection.  The rest have `conservation_status` equal to `None`.  Because `groupby` does not include `None`, we will need to fill in the null values.  We can do this using `.fillna`.  We pass in however we want to fill in our `None` values as an argument.\n",
    "\n",
    "Paste the following code and run it to see replace `None` with `No Intervention`:\n",
    "```python\n",
    "species.fillna('No Intervention', inplace=True)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "species.fillna('No Intervention', inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now run the same `groupby` as before to see how many species require `No Protection`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>scientific_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Endangered</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>In Recovery</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>No Intervention</td>\n",
       "      <td>5363</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>151</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Threatened</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  conservation_status  scientific_name\n",
       "0          Endangered               15\n",
       "1         In Recovery                4\n",
       "2     No Intervention             5363\n",
       "3  Species of Concern              151\n",
       "4          Threatened               10"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.groupby('conservation_status').scientific_name.nunique().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's use `plt.bar` to create a bar chart.  First, let's sort the columns by how many species are in each categories.  We can do this using `.sort_values`.  We use the the keyword `by` to indicate which column we want to sort by.\n",
    "\n",
    "Paste the following code and run it to create a new DataFrame called `protection_counts`, which is sorted by `scientific_name`:\n",
    "```python\n",
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.count().reset_index()\\\n",
    "    .sort_values(by='scientific_name')\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.nunique().reset_index()\\\n",
    "    .sort_values(by='scientific_name')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's create a bar chart!\n",
    "1. Start by creating a wide figure with `figsize=(10, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `scientific_name` column of `protection_counts`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `conservation_status` in `protection_counts`\n",
    "5. Label the y-axis `Number of Species`\n",
    "6. Title the graph `Conservation Status by Species`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n8Nft6tJdgZtbV+rXgN2SbNwuStitlUmSJK1WxtlVugXwpSQT6/lMVf13ku8Bxyd5CXAV8JxW/xTg\nqcAVwO3A/gBVdUOSw4HvtXqHVdUNY4xbkiRppTS2xK2qrgT+YoryXwJPnKK8gAOHLOsY4JgVHaMk\nSVKf+M8JkiRJPWHiJkmS1BMmbpIkST1h4iZJktQTJm6SJEk9YeImSZLUEyZukiRJPWHiJkmS1BMm\nbpIkST1h4iZJktQTJm6SJEk9YeImSZLUEyZukiRJPWHiJkmS1BMmbpIkST1h4iZJktQTJm6SJEk9\nYeImSZLUEyZukiRJPWHiJkmS1BMmbpIkST1h4iZJktQTJm6SJEk9YeImSZLUEyZukiRJPWHiJkmS\n1BMmbpIkST1h4iZJktQTJm6SJEk9MfbELcmaSc5PclIb3y7Jd5NcnuRzSdZp5eu28Sva9PkDyzik\nlf8oyZPHHbMkSdLKaDZa3A4CLhsYPwJ4b1XtANwIvKSVvwS4saq2B97b6pFkR2Af4MHA7sBRSdac\nhbglSZJWKmNN3JJsDewBfKSNB3gCcEKrciywVxves43Tpj+x1d8TOK6q7qiqnwBXAA8fZ9ySJEkr\no3G3uL0PeB3w+za+KXBTVd3ZxhcBW7XhrYCrAdr0m1v9P5RPMc8fJDkgyblJzl28ePGK3g5JkqQ5\nN2PiluQ5STZow4cm+WKSnUeY72nA9VV13mDxFFVrhmnTzXN3QdXRVbWgqhbMmzdvpvAkSZJ6Z5QW\nt3+tqluTPAp4Ml135odGmO+RwDOSLASOo+sifR+wUZK1Wp2tgWvb8CJgG4A2fUPghsHyKeaRJEla\nbYySuN3VnvcAPlRVXwHWmWmmqjqkqrauqvl0Fxd8o6r2Bc4A9m7V9gO+0oZPbOO06d+oqmrl+7Sr\nTrcDdgDOGSFuSZKkVcooids1ST4MPBc4Jcm6I843zOuBVyW5gu4cto+28o8Cm7byVwEHA1TVJcDx\nwKXAfwMHVtVdSy1VkiRpFbfWzFV4Lt1tON5dVTcl2RJ47bKspKrOBM5sw1cyxVWhVfUb4DlD5n8r\n8NZlWackSdKqZsaWs6q6HbgeeFQruhO4fJxBSZIkaWmjXFX6RrruzUNa0drAp8YZlCRJkpY2yrlq\nzwSeAfwKoKquBTYYZ1CSJEla2iiJ22/b1Z0FkGT98YYkSZKkqYySuB3frirdKMnfAV8H/nO8YUmS\n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\nRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x114e89ad0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10, 4))\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(protection_counts)),\n",
    "        protection_counts.scientific_name.values)\n",
    "ax.set_xticks(range(len(protection_counts)))\n",
    "ax.set_xticklabels(protection_counts.conservation_status.values)\n",
    "plt.ylabel('Number of Species')\n",
    "plt.title('Conservation Status by Species')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Are certain types of species more likely to be endangered?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column in `species` called `is_protected`, which is `True` if `conservation_status` is not equal to `No Intervention`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "species['is_protected'] = species.conservation_status != 'No Intervention'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's group by *both* `category` and `is_protected`.  Save your results to `category_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "category_counts = species.groupby(['category', 'is_protected'])\\\n",
    "                         .scientific_name.nunique().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_counts` using `head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>scientific_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Amphibian</td>\n",
       "      <td>False</td>\n",
       "      <td>72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Amphibian</td>\n",
       "      <td>True</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Bird</td>\n",
       "      <td>False</td>\n",
       "      <td>413</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Bird</td>\n",
       "      <td>True</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Fish</td>\n",
       "      <td>False</td>\n",
       "      <td>115</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    category  is_protected  scientific_name\n",
       "0  Amphibian         False               72\n",
       "1  Amphibian          True                7\n",
       "2       Bird         False              413\n",
       "3       Bird          True               75\n",
       "4       Fish         False              115"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category_counts.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "It's going to be easier to view this data if we pivot it.  Using `pivot`, rearange `category_counts` so that:\n",
    "- `columns` is `is_protected`\n",
    "- `index` is `category`\n",
    "- `values` is `scientific_name`\n",
    "\n",
    "Save your pivoted data to `category_pivot`. Remember to `reset_index()` at the end."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "category_pivot = category_counts.pivot(columns='is_protected',\n",
    "                                      index='category',\n",
    "                                      values='scientific_name')\\\n",
    "                                .reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_protected</th>\n",
       "      <th>category</th>\n",
       "      <th>False</th>\n",
       "      <th>True</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Amphibian</td>\n",
       "      <td>72</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bird</td>\n",
       "      <td>413</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Fish</td>\n",
       "      <td>115</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>146</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Nonvascular Plant</td>\n",
       "      <td>328</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Reptile</td>\n",
       "      <td>73</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>4216</td>\n",
       "      <td>46</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_protected           category  False  True\n",
       "0                     Amphibian     72     7\n",
       "1                          Bird    413    75\n",
       "2                          Fish    115    11\n",
       "3                        Mammal    146    30\n",
       "4             Nonvascular Plant    328     5\n",
       "5                       Reptile     73     5\n",
       "6                Vascular Plant   4216    46"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `.columns` property to  rename the categories `True` and `False` to something more description:\n",
    "- Leave `category` as `category`\n",
    "- Rename `False` to `not_protected`\n",
    "- Rename `True` to `protected`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "category_pivot.columns = ['category', 'not_protected', 'protected']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column of `category_pivot` called `percent_protected`, which is equal to `protected` (the number of species that are protected) divided by `protected` plus `not_protected` (the total number of species)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "category_pivot['percent_protected'] = category_pivot.protected / \\\n",
    "                                      (category_pivot.protected + category_pivot.not_protected)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>not_protected</th>\n",
       "      <th>protected</th>\n",
       "      <th>percent_protected</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Amphibian</td>\n",
       "      <td>72</td>\n",
       "      <td>7</td>\n",
       "      <td>0.088608</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bird</td>\n",
       "      <td>413</td>\n",
       "      <td>75</td>\n",
       "      <td>0.153689</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Fish</td>\n",
       "      <td>115</td>\n",
       "      <td>11</td>\n",
       "      <td>0.087302</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>146</td>\n",
       "      <td>30</td>\n",
       "      <td>0.170455</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Nonvascular Plant</td>\n",
       "      <td>328</td>\n",
       "      <td>5</td>\n",
       "      <td>0.015015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Reptile</td>\n",
       "      <td>73</td>\n",
       "      <td>5</td>\n",
       "      <td>0.064103</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>4216</td>\n",
       "      <td>46</td>\n",
       "      <td>0.010793</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            category  not_protected  protected  percent_protected\n",
       "0          Amphibian             72          7           0.088608\n",
       "1               Bird            413         75           0.153689\n",
       "2               Fish            115         11           0.087302\n",
       "3             Mammal            146         30           0.170455\n",
       "4  Nonvascular Plant            328          5           0.015015\n",
       "5            Reptile             73          5           0.064103\n",
       "6     Vascular Plant           4216         46           0.010793"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like species in category `Mammal` are more likely to be endangered than species in `Bird`.  We're going to do a significance test to see if this statement is true.  Before you do the significance test, consider the following questions:\n",
    "- Is the data numerical or categorical?\n",
    "- How many pieces of data are you comparing?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on those answers, you should choose to do a *chi squared test*.  In order to run a chi squared test, we'll need to create a contingency table.  Our contingency table should look like this:\n",
    "\n",
    "||protected|not protected|\n",
    "|-|-|-|\n",
    "|Mammal|?|?|\n",
    "|Bird|?|?|\n",
    "\n",
    "Create a table called `contingency` and fill it in with the correct numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "contingency = [[30, 146],\n",
    "              [75, 413]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to perform our chi square test, we'll need to import the correct function from scipy.  Past the following code and run it:\n",
    "```py\n",
    "from scipy.stats import chi2_contingency\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from scipy.stats import chi2_contingency"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now run `chi2_contingency` with `contingency`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.16170148316545571,\n",
       " 0.68759480966613362,\n",
       " 1,\n",
       " array([[  27.8313253,  148.1686747],\n",
       "        [  77.1686747,  410.8313253]]))"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "chi2_contingency(contingency)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like this difference isn't significant!\n",
    "\n",
    "Let's test another.  Is the difference between `Reptile` and `Mammal` significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4.2891830962036446,\n",
       " 0.038355590229698977,\n",
       " 1,\n",
       " array([[  24.2519685,  151.7480315],\n",
       "        [  10.7480315,   67.2519685]]))"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "contingency = [[30, 146],\n",
    "               [5, 73]]\n",
    "chi2_contingency(contingency)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Yes! It looks like there is a significant difference between `Reptile` and `Mammal`!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Conservationists have been recording sightings of different species at several national parks for the past 7 days.  They've saved sent you their observations in a file called `observations.csv`.  Load `observations.csv` into a variable called `observations`, then use `head` to view the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>park_name</th>\n",
       "      <th>observations</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Vicia benghalensis</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Neovison vison</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Prunus subcordata</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>138</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Abutilon theophrasti</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>84</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Githopsis specularioides</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            scientific_name                            park_name  observations\n",
       "0        Vicia benghalensis  Great Smoky Mountains National Park            68\n",
       "1            Neovison vison  Great Smoky Mountains National Park            77\n",
       "2         Prunus subcordata               Yosemite National Park           138\n",
       "3      Abutilon theophrasti                  Bryce National Park            84\n",
       "4  Githopsis specularioides  Great Smoky Mountains National Park            85"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "observations = pd.read_csv('observations.csv')\n",
    "observations.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Some scientists are studying the number of sheep sightings at different national parks.  There are several different scientific names for different types of sheep.  We'd like to know which rows of `species` are referring to sheep.  Notice that the following code will tell us whether or not a word occurs in a string:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str1 = 'This string contains Sheep'\n",
    "'Sheep' in str1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str2 = 'This string contains Cows'\n",
    "'Sheep' in str2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use `apply` and a `lambda` function to create a new column in `species` called `is_sheep` which is `True` if the `common_names` contains `'Sheep'`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Clethrionomys gapperi gapperi</td>\n",
       "      <td>Gapper's Red-Backed Vole</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos bison</td>\n",
       "      <td>American Bison, Bison</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos taurus</td>\n",
       "      <td>Aurochs, Aurochs, Domestic Cattle (Feral), Dom...</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Cervus elaphus</td>\n",
       "      <td>Wapiti Or Elk</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  category                scientific_name  \\\n",
       "0   Mammal  Clethrionomys gapperi gapperi   \n",
       "1   Mammal                      Bos bison   \n",
       "2   Mammal                     Bos taurus   \n",
       "3   Mammal                     Ovis aries   \n",
       "4   Mammal                 Cervus elaphus   \n",
       "\n",
       "                                        common_names conservation_status  \\\n",
       "0                           Gapper's Red-Backed Vole     No Intervention   \n",
       "1                              American Bison, Bison     No Intervention   \n",
       "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...     No Intervention   \n",
       "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "4                                      Wapiti Or Elk     No Intervention   \n",
       "\n",
       "   is_protected  is_sheep  \n",
       "0         False     False  \n",
       "1         False     False  \n",
       "2         False     False  \n",
       "3         False      True  \n",
       "4         False     False  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)\n",
    "species.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Select the rows of `species` where `is_sheep` is `True` and examine the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1139</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Rumex acetosella</td>\n",
       "      <td>Sheep Sorrel, Sheep Sorrell</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2233</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Festuca filiformis</td>\n",
       "      <td>Fineleaf Sheep Fescue</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3014</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3758</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Rumex acetosella</td>\n",
       "      <td>Common Sheep Sorrel, Field Sorrel, Red Sorrel,...</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3761</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Rumex paucifolius</td>\n",
       "      <td>Alpine Sheep Sorrel, Fewleaved Dock, Meadow Dock</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4091</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Carex illota</td>\n",
       "      <td>Sheep Sedge, Smallhead Sedge</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4383</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Potentilla ovina var. ovina</td>\n",
       "      <td>Sheep Cinquefoil</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4446</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            category              scientific_name  \\\n",
       "3             Mammal                   Ovis aries   \n",
       "1139  Vascular Plant             Rumex acetosella   \n",
       "2233  Vascular Plant           Festuca filiformis   \n",
       "3014          Mammal              Ovis canadensis   \n",
       "3758  Vascular Plant             Rumex acetosella   \n",
       "3761  Vascular Plant            Rumex paucifolius   \n",
       "4091  Vascular Plant                 Carex illota   \n",
       "4383  Vascular Plant  Potentilla ovina var. ovina   \n",
       "4446          Mammal      Ovis canadensis sierrae   \n",
       "\n",
       "                                           common_names conservation_status  \\\n",
       "3     Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "1139                        Sheep Sorrel, Sheep Sorrell     No Intervention   \n",
       "2233                              Fineleaf Sheep Fescue     No Intervention   \n",
       "3014                       Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
       "3758  Common Sheep Sorrel, Field Sorrel, Red Sorrel,...     No Intervention   \n",
       "3761   Alpine Sheep Sorrel, Fewleaved Dock, Meadow Dock     No Intervention   \n",
       "4091                       Sheep Sedge, Smallhead Sedge     No Intervention   \n",
       "4383                                   Sheep Cinquefoil     No Intervention   \n",
       "4446                        Sierra Nevada Bighorn Sheep          Endangered   \n",
       "\n",
       "      is_protected  is_sheep  \n",
       "3            False      True  \n",
       "1139         False      True  \n",
       "2233         False      True  \n",
       "3014          True      True  \n",
       "3758         False      True  \n",
       "3761         False      True  \n",
       "4091         False      True  \n",
       "4383         False      True  \n",
       "4446          True      True  "
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species[species.is_sheep]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Many of the results are actually plants.  Select the rows of `species` where `is_sheep` is `True` and `category` is `Mammal`.  Save the results to the variable `sheep_species`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3014</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4446</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     category          scientific_name  \\\n",
       "3      Mammal               Ovis aries   \n",
       "3014   Mammal          Ovis canadensis   \n",
       "4446   Mammal  Ovis canadensis sierrae   \n",
       "\n",
       "                                           common_names conservation_status  \\\n",
       "3     Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "3014                       Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
       "4446                        Sierra Nevada Bighorn Sheep          Endangered   \n",
       "\n",
       "      is_protected  is_sheep  \n",
       "3            False      True  \n",
       "3014          True      True  \n",
       "4446          True      True  "
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]\n",
    "sheep_species"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now merge `sheep_species` with `observations` to get a DataFrame with observations of sheep.  Save this DataFrame as `sheep_observations`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>park_name</th>\n",
       "      <th>observations</th>\n",
       "      <th>category</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>219</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>109</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>117</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>48</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>67</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>39</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>22</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>25</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>126</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>76</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>119</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>221</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            scientific_name                            park_name  \\\n",
       "0           Ovis canadensis            Yellowstone National Park   \n",
       "1           Ovis canadensis                  Bryce National Park   \n",
       "2           Ovis canadensis               Yosemite National Park   \n",
       "3           Ovis canadensis  Great Smoky Mountains National Park   \n",
       "4   Ovis canadensis sierrae            Yellowstone National Park   \n",
       "5   Ovis canadensis sierrae               Yosemite National Park   \n",
       "6   Ovis canadensis sierrae                  Bryce National Park   \n",
       "7   Ovis canadensis sierrae  Great Smoky Mountains National Park   \n",
       "8                Ovis aries               Yosemite National Park   \n",
       "9                Ovis aries  Great Smoky Mountains National Park   \n",
       "10               Ovis aries                  Bryce National Park   \n",
       "11               Ovis aries            Yellowstone National Park   \n",
       "\n",
       "    observations category                                       common_names  \\\n",
       "0            219   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
       "1            109   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
       "2            117   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
       "3             48   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
       "4             67   Mammal                        Sierra Nevada Bighorn Sheep   \n",
       "5             39   Mammal                        Sierra Nevada Bighorn Sheep   \n",
       "6             22   Mammal                        Sierra Nevada Bighorn Sheep   \n",
       "7             25   Mammal                        Sierra Nevada Bighorn Sheep   \n",
       "8            126   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
       "9             76   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
       "10           119   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
       "11           221   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
       "\n",
       "   conservation_status  is_protected  is_sheep  \n",
       "0   Species of Concern          True      True  \n",
       "1   Species of Concern          True      True  \n",
       "2   Species of Concern          True      True  \n",
       "3   Species of Concern          True      True  \n",
       "4           Endangered          True      True  \n",
       "5           Endangered          True      True  \n",
       "6           Endangered          True      True  \n",
       "7           Endangered          True      True  \n",
       "8      No Intervention         False      True  \n",
       "9      No Intervention         False      True  \n",
       "10     No Intervention         False      True  \n",
       "11     No Intervention         False      True  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sheep_observations = observations.merge(sheep_species)\n",
    "sheep_observations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many total sheep observations (across all three species) were made at each national park?  Use `groupby` to get the `sum` of `observations` for each `park_name`.  Save your answer to `obs_by_park`.\n",
    "\n",
    "This is the total number of sheep observed in each park over the past 7 days."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>park_name</th>\n",
       "      <th>observations</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>282</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             park_name  observations\n",
       "0                  Bryce National Park           250\n",
       "1  Great Smoky Mountains National Park           149\n",
       "2            Yellowstone National Park           507\n",
       "3               Yosemite National Park           282"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()\n",
    "obs_by_park"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a bar chart showing the different number of observations per week at each park.\n",
    "\n",
    "1. Start by creating a wide figure with `figsize=(16, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `observations` column of `obs_by_park`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `park_name` in `obs_by_park`\n",
    "5. Label the y-axis `Number of Observations`\n",
    "6. Title the graph `Observations of Sheep per Week`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n6j+TbNPuk5xLd//kPOAbfbM/McmOrXb3LXQJxSlJHp5kq9YZ0m3ArXS1sgBfAD7Ua/qZZE6S7acI\n60d0yeH76e6ZvbuVr0yXiF4DLJPkPcAqfcv9EZg7WadHdAnzvyR5SJKVmH9P7qBm2PeS5FVJ5rRY\nrm/Fdw2Y9VvAa5Ns1l6PDwOntg65ptrGI1qN9AZtfEO65sCTNXu+R1VdBRwNfDLJKuk6ytokybPa\nLF8A3pnk0W3dqybZacJq3p5k9bbdveg6bJrMwGMBOA24MV1nYismWTrJYzL9vyw6sa23PwE9uZX9\nodfUfSHt95V09wLvmeQN04xTkjTDTGwlSSOpqo/RNRf9BHAjcCpdTdfWEzo4Ohx4OV0HUK8Gdmz3\nWC4P7EfXbPkPdLWa72rLfBo4Ajg6yU10yc+Tp4jndrrOrJ5Llyj2/ISuQ6v/o2sqexv3btb63fZ8\nbZKzBqz6K3SJ+onA79rybx4WS59tgAuS3Nz2aedWszgx9mOBfwe+R3eP8ibc+/7SYW6ie21OTfIX\nutfqfOBtIy7/GroehH9F9x4dQtecnKo6lK6m+TvpeiM+n65Gvt/hwJnAL+mag395yLYGHgvt3t8X\n0XXw9Tu6Y+JLdE3Gp+MEuuPo5L6yk1vZxL/5ub/7TbuveGtg77RetCVJi4dUTdUiS5Ikqfu7H2DT\ndr/0VPPuCzysql411bySJN1f1thKkiRJksaaia0kSZIkaazZFFmSJEmSNNassZUkSZIkjbVlZjuA\n+2OttdaquXPnznYYkiRJkqQZcOaZZ/6pquZMNd9YJ7Zz587ljDPOmO0wJEmSJEkzIMllo8xnU2RJ\nkiRJ0lgzsZUkSZIkjTUTW0mSJEnSWDOxlSRJkiSNNRNbSZIkSdJYM7GVJEmSJI01E1tJkiRJ0lgz\nsZUkSZIkjbUZTWyTXJrkvCS/THJGK1sjyTFJLmrPq7fyJPlMkouTnJvkCTMZmyRJkiTpgWGZRbCN\n51TVn/rG9wGOrar9kuzTxvcGtgU2bY8nA59vz5IkaQbN3eeHsx2CNJJL93vBbIcgaTE1G02RtwcO\nbMMHAjv0lX+9OqcAqyVZdxbikyRJkiSNkZlObAs4OsmZSfZoZetU1VUA7XntVr4+cEXfsvNamSRJ\nkiRJk5rppshPq6ork6wNHJPk10PmzYCyus9MXYK8B8BGG220cKKUJEmSJI2tGa2xraor2/PVwKHA\nk4A/9poYt+er2+zzgA37Ft8AuHLAOg+oqs2ravM5c+bMZPiSJEmSpDEwY4ltkgcnWbk3DDwfOB84\nAtilzbYLcHgbPgJ4TesdeUvghl6TZUmSJEmSJjOTTZHXAQ5N0tvOt6rqqCSnAwcn2Q24HNipzf8j\nYDvgYuAW4LUzGJskSZIk6QFixhLbqroEeNyA8muBrQeUF/DGmYpHkiRJkvTANBt/9yNJkiRJ0kJj\nYitJkiRJGmsmtpIkSZKksWZiK0mSJEkaaya2kiRJkqSxZmIrSZIkSRprJraSJEmSpLFmYitJkiRJ\nGmsmtpIkSZKksWZiK0mSJEkaaya2kiRJkqSxZmIrSZIkSRprJraSJEmSpLFmYitJkiRJGmsmtpIk\nSZKksWZiK0mSJEkaaya2kiRJkqSxZmIrSZIkSRprJraSJEmSpLFmYitJkiRJGmsmtpIkSZKksWZi\nK0mSJEkaaya2kiRJkqSxZmIrSZIkSRprJraSJEmSpLFmYitJkiRJGmsmtpIkSZKksWZiK0mSJEka\naya2kiRJkqSxZmIrSZIkSRprJraSJEmSpLE2rcQ2yepJHjtTwUiSJEmSNF1TJrZJjk+ySpI1gHOA\nrybZf9QNJFk6ydlJjmzjD0lyapKLkhyUZLlWvnwbv7hNn7tguyRJkiRJWpKMUmO7alXdCOwIfLWq\nngg8dxrb2Au4sG/8o8CnqmpT4Dpgt1a+G3BdVT0M+FSbT5IkSZKkoUZJbJdJsi7wMuDI6aw8yQbA\nC4AvtfEAWwGHtFkOBHZow9u3cdr0rdv8kiRJkiRNapTE9v3AT4CLq+r0JA8FLhpx/f8BvAO4u42v\nCVxfVXe28XnA+m14feAKgDb9hjb/vSTZI8kZSc645pprRgxDkiRJkvRANWViW1XfrarHVtUb2vgl\nVfUPUy2X5IXA1VV1Zn/xoE2MMK0/ngOqavOq2nzOnDlThSFJkiRJeoBbZqoZkswB/gmY2z9/Vb1u\nikWfBrw4yXbACsAqdDW4qyVZptXKbgBc2eafB2wIzEuyDLAq8Odp7Y0kSZIkaYkzSlPkw+mSzJ8C\nP+x7DFVV76yqDapqLrAz8LOqeiVwHPDSNtsubf0AR7Rx2vSfVdV9amwlSZIkSeo3ZY0t8KCq2nsh\nbnNv4DtJPgicDXy5lX8Z+EaSi+lqandeiNuUJEmSJD1AjZLYHplku6r60YJupKqOB45vw5cATxow\n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\naya2kiRJkqSxZmIrSZIkSRprJraSJEmSpLFmYitJkiRJGmsmtpIkSZKksWZiK0mSJEkaaya2kiRJ\nkqSxZmIrSZIkSRprJraSJEmSpLFmYitJkiRJGmsmtpIkSZKksWZiK0mSJEkaaya2kiRJkqSxZmIr\nSZIkSRpri1Vim2SbJL9JcnGSfWY7HkmSJEnS4m+xSWyTLA18DtgWeBTwiiSPmt2oJEmSJEmLu8Um\nsQWeBFxcVZdU1R3Ad4DtZzkmSZIkSdJiLlU12zEAkOSlwDZVtXsbfzXw5Kp604T59gD2aKMPB36z\nSAPV4mAt4E+zHYT0AON5JS1cnlPSwud5tWTauKrmTDXTMosikhFlQNl9su6qOgA4YObD0eIqyRlV\ntflsxyE9kHheSQuX55S08HleaZjFqSnyPGDDvvENgCtnKRZJkiRJ0phYnBLb04FNkzwkyXLAzsAR\nsxyTJEmSJGkxt9g0Ra6qO5O8CfgJsDTwlaq6YJbD0uLJpujSwud5JS1cnlPSwud5pUktNp1HSZIk\nSZK0IBanpsiSJEmSJE2bia0kSZIkaayZ2C6BktyV5JdJzklyVpKnLsJt75rk7iSP7Ss7P8ncKZZ7\nS5IH9Y3/KMlqCzm2fZP86yTlv2+v2flJXjzN9e6a5LMLL9IHtiTrJPlWkkuSnJnkF0leshDX/64h\n016X5Lwk57b3evuFsL25Sc5fwGWfnaSS7NZX9vhWdp9j9f4a9tpMmO9+n399+/aivrIjkzx7iuV2\nTbJe3/iXkjzq/sQyyTbuc8628mvaZ8GvkvzTNNf77CRHLrxIF1/pnJxk276ylyU5asgy85KslmSZ\nJNfPUFxvTbLCTKy7bxvPbcd2/74fleTpUyz3uiR/0zf+1SQPX8ix7Z7kPyYp7x3bFyZ53TTX+9wk\nhy28SDVdC3LOzUAMSyc5qQ0/NMnO01x+mXbufLSvbJ8k755iua2SbNk3/sYkr5xu/FNs42FJfjlJ\n+a193wufSzLoL0wnW++Mfd4tiUxsl0y3VtVmVfU44J3ARybOkGTpGdz+PODfprnMW4B7Etuq2q6q\nFuUHwaeqajNgJ+ArSUY6d5IsNh20jYP2ZXAYcGJVPbSqnkjXQ/oGA+Zd0Nd2YPKWZAO64/LpVfVY\nYEvg3AXcxsJ0HvDyvvGdgXNmaFsjJbYL8fxbkM+CXYF7Etuq2r2qfrUQYhnVQe2z4NnAh5OsM8pC\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1a1f498e50>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16, 4))\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(obs_by_park)),\n",
    "        obs_by_park.observations.values)\n",
    "ax.set_xticks(range(len(obs_by_park)))\n",
    "ax.set_xticklabels(obs_by_park.park_name.values)\n",
    "plt.ylabel('Number of Observations')\n",
    "plt.title('Observations of Sheep per Week')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Our scientists know that 15% of sheep at Bryce National Park have foot and mouth disease.  Park rangers at Yellowstone National Park have been running a program to reduce the rate of foot and mouth disease at that park.  The scientists want to test whether or not this program is working.  They want to be able to detect reductions of at least 5 percentage point.  For instance, if 10% of sheep in Yellowstone have foot and mouth disease, they'd like to be able to know this, with confidence.\n",
    "\n",
    "Use the <a href=\"https://s3.amazonaws.com/codecademy-content/courses/learn-hypothesis-testing/a_b_sample_size/index.html\">Codecademy sample size calculator</a> to calculate the number of sheep that they would need to observe from each park.  Use the default level of significance (90%).\n",
    "\n",
    "Remember that \"Minimum Detectable Effect\" is a percent of the baseline."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "33.333333333333336"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "minimum_detectable_effect = 100 * 0.05 / 0.15\n",
    "minimum_detectable_effect"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "baseline = 15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sample_size_per_variant = 870\n",
    "# Note: This could be 890 if you used 33% for the \"Minimum Detectable Effect\" instead of 33.33%.  That's fine."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many weeks would you need to observe sheep at Bryce National Park in order to observe enough sheep?  How many weeks would you need to observe at Yellowstone National Park to observe enough sheep?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "bryce = 870 / 250.\n",
    "yellowstone = 810 / 507.\n",
    "\n",
    "# Approximately 3.5 weeks at Bryce and 1.5 weeks at Yellowstone."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
