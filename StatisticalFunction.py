{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "880f66fc-ee5d-4d06-af13-2cc4fefe6176",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data: [10 20 30 40 50 60]\n",
      "Mean: 35.0\n",
      "Standard Deviation: 17.07825127659933\n",
      "Variance: 291.6666666666667\n",
      "50th Percentile (Median): 35.0\n",
      "Minimum Value: 10\n",
      "Maximum Value: 60\n",
      "Cumulative Sum: [ 10  30  60 100 150 210]\n",
      "Cumulative Product: [       10       200      6000    240000  12000000 720000000]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Step 1: Create a NumPy array\n",
    "data = np.array([10, 20, 30, 40, 50, 60])\n",
    "\n",
    "# Step 2: Compute Statistical Measures\n",
    "mean_value = np.mean(data)            \n",
    "std_dev = np.std(data)                \n",
    "variance = np.var(data)                \n",
    "percentile_50 = np.percentile(data, 50) \n",
    "min_value = np.min(data)               \n",
    "max_value = np.max(data)              \n",
    "cumulative_sum = np.cumsum(data)       \n",
    "cumulative_product = np.cumprod(data) \n",
    "\n",
    "# Step 3: Display Results\n",
    "print(\"Data:\", data)\n",
    "print(\"Mean:\", mean_value)\n",
    "print(\"Standard Deviation:\", std_dev)\n",
    "print(\"Variance:\", variance)\n",
    "print(\"50th Percentile (Median):\", percentile_50)\n",
    "print(\"Minimum Value:\", min_value)\n",
    "print(\"Maximum Value:\", max_value)\n",
    "print(\"Cumulative Sum:\", cumulative_sum)\n",
    "print(\"Cumulative Product:\", cumulative_product)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4162e90-8dec-4033-810d-32d17e12a81a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:anaconda3]",
   "language": "python",
   "name": "conda-env-anaconda3-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
