---
layout: default
title: Quantum Approaches to Urban Logistics: From Core QAOA to Clustered Scalability
---

# Quantum Approaches to Urban Logistics: From Core QAOA to Clustered Scalability

**arXiv**: [2512.10813v1](https://arxiv.org/abs/2512.10813) | [PDF](https://arxiv.org/pdf/2512.10813.pdf)

**作者**: F. Picariello, G. Turati, R. Antonelli, I. Bailo, S. Bonura, G. Ciarfaglia, S. Cipolla, P. Cremonesi, M. Ferrari Dacrema, M. Gabusi, I. Gentile, V. Morreale, A. Noto

---

## 💡 一句话要点

**提出聚类QAOA以解决带约束旅行商问题的量子优化可扩展性**

**关键词**: `量子近似优化算法` `旅行商问题` `城市物流` `量子优化` `可扩展性` `混合量子经典方法`

## 📋 核心要点

1. 研究量子近似优化算法在带现实约束旅行商问题中的应用
2. 提出聚类QAOA方法，结合经典机器学习分解大问题以提高可扩展性
3. 通过高性能计算模拟评估算法在不同规模和深度下的性能

## 📄 摘要（原文）

> The Traveling Salesman Problem (TSP) is a fundamental challenge in combinatorial optimization, widely applied in logistics and transportation. As the size of TSP instances grows, traditional algorithms often struggle to produce high-quality solutions within reasonable timeframes. This study investigates the potential of the Quantum Approximate Optimization Algorithm (QAOA), a hybrid quantum-classical method, to solve TSP under realistic constraints. We adopt a QUBO-based formulation of TSP that integrates real-world logistical constraints reflecting operational conditions, such as vehicle capacity, road accessibility, and time windows, while ensuring compatibility with the limitations of current quantum hardware. Our experiments are conducted in a simulated environment using high-performance computing (HPC) resources to assess QAOA's performance across different problem sizes and quantum circuit depths. In order to improve scalability, we propose clustering QAOA (Cl-QAOA), a hybrid approach combining classical machine learning with QAOA. This method decomposes large TSP instances into smaller sub-problems, making quantum optimization feasible even on devices with a limited number of qubits. The results offer a comprehensive evaluation of QAOA's strengths and limitations in solving constrained TSP scenarios. This study advances quantum optimization and lays groundwork for future large-scale applications.

