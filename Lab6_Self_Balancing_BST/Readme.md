# Self-Balancing Binary Search Tree – DSA Lab 6

## Project Overview

This project implements and compares a standard Binary Search Tree (BST) and an AVL Tree for managing patient records in a simulated MediQueue telemedicine system. Each patient record contains an integer Patient ID and a Patient Name.

The main objective is to understand how tree balancing affects insertion, searching, deletion, and overall performance, particularly when records are inserted in sequential order.

## Objectives

- Implement a Plain Binary Search Tree with insertion, searching, deletion, and in-order traversal.
- Implement an AVL Tree with automatic balancing.
- Apply all four AVL rotation cases: LL, RR, LR, and RL.
- Generate sequential, random, and nearly sorted datasets.
- Compare tree height, insertion time, search comparisons, and rotations.
- Explore alternative tree structures through self-learning.

## Implementations

### 1. Plain Binary Search Tree

The Plain BST stores patient records according to their Patient ID. It supports insertion, searching, deletion, in-order traversal, height calculation, and key-comparison counting. Iterative insertion is used to handle large sequential datasets without recursive-depth issues.

### 2. AVL Tree

The AVL Tree is a self-balancing BST. Each node stores its height, and the balance factor is used to identify imbalance. Rotations are performed after insertion and deletion to maintain AVL balance.

### 3. Self-Learning Implementations

The project also includes independent implementations and testing of:

- Red-Black Tree – uses node colours, recolouring, and rotations.
- Treap – combines BST ordering with randomly assigned priorities.
- Splay Tree – adjusts the tree structure when nodes are accessed.

## Dataset Generation

Experiments are performed using three input patterns:

1. **Sequential:** Patient IDs in ascending order.
2. **Random:** A random permutation of Patient IDs.
3. **Nearly Sorted:** Ascending IDs with approximately 5% of positions randomly swapped.

The dataset sizes are 1,000, 5,000, and 10,000. A fixed random seed is used to support reproducibility.

## Performance Evaluation

Both the Plain BST and AVL Tree are evaluated using:

- Final tree height after insertion.
- Theoretical minimum height reference.
- Total insertion time.
- Average comparisons across 1,000 successful searches.
- AVL rotations.
- Tree height after deleting 20% of the keys.

The results are exported to CSV, and a graph is generated to compare tree heights for sequential input.

## Tools and Technologies

- Python
- Google Colab / Jupyter Notebook
- Matplotlib for graph generation
- CSV for storing experiment results

No built-in balanced-tree library is used for the core BST or AVL implementation. The tree node structures and operations are implemented manually.

## How to Run

1. Download or clone this repository.
2. Open `source/Dsa_Lab6.ipynb` in Google Colab or Jupyter Notebook.
3. Run the notebook cells in order, from setup and implementation through testing and experiments.
4. Execute the experiment section to generate the comparison results.
5. Run the CSV export and graph-generation sections to produce the output files.

## Project Structure

```text
DSA-Lab6-Self-Balancing-BST/
│
├── README.md
├── source/
│   └── Dsa_Lab6.ipynb
├── results/
│   ├── lab6_bst_avl_results.csv
│   └── lab6_sequential_height_comparison.png
├── report/
│   └── DSA_Lab6_Report.docx
└── screenshots/
    └── experiment screenshots
```

## Conclusion

This project demonstrates how the structure of a Binary Search Tree affects its performance. A Plain BST can become unbalanced when sequential keys are inserted, whereas an AVL Tree maintains logarithmic height through rotations. The additional self-learning implementations provide further understanding of different balancing and self-adjusting techniques.

## Academic Context

**Programme:** M.Sc. Artificial Intelligence and Machine Learning  
**Course Area:** Data Structures and Algorithms  
**Lab Activity:** Self-Balancing Binary Search Tree – Lab 6