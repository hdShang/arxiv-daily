---
layout: default
title: Continual Learning at the Edge: An Agnostic IIoT Architecture
---

# Continual Learning at the Edge: An Agnostic IIoT Architecture

**arXiv**: [2512.14311v1](https://arxiv.org/abs/2512.14311) | [PDF](https://arxiv.org/pdf/2512.14311.pdf)

**作者**: Pablo García-Santaclara, Bruno Fernández-Castro, Rebeca P. Díaz-Redondo, Carlos Calvo-Moa, Henar Mariño-Bodelón

**分类**: stat.ML, cs.LG

**发布日期**: 2025-12-16

**期刊**: García-Santaclara, P., Fernández-Castro, B., Díaz-Redondo, R. P., Calvo-Moa, C., & Mariño-Bodelón, H. (2025). Continual learning at the edge: An agnostic IIoT architecture. In Lecture Notes in Networks and Systems. Springer

**DOI**: [10.1007/978-981-96-6938-7_33](https://doi.org/10.1007/978-981-96-6938-7_33)

---

## 💡 一句话要点

**提出一种边缘计算场景下的增量学习方法，用于工业物联网实时质量控制，减少灾难性遗忘影响。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `边缘计算` `增量学习` `工业物联网` `实时质量控制` `灾难性遗忘` `制造系统` `动态数据流`

## 📋 核心要点

1. 传统集中式计算系统面临延迟和带宽限制，边缘计算虽能缓解但数据动态连续到达，传统机器学习算法难以适应。
2. 提出在工业边缘计算场景中应用增量学习，通过持续学习机制减少灾难性遗忘，实现实时质量控制。
3. 该方法在制造系统中提供高效解决方案，降低遗忘影响，提升边缘设备的学习效率和适应性。

## 📝 摘要（中文）

互联网连接设备的指数级增长给传统集中式计算系统带来了延迟和带宽限制的挑战。边缘计算通过将计算更靠近数据源来解决这些困难。此外，传统机器学习算法不适合边缘计算系统，因为数据通常以动态和连续的方式到达。然而，增量学习为这些场景提供了良好的解决方案。我们引入了一种新方法，将增量学习理念应用于工业领域的边缘计算场景，具体目的是在制造系统中实现实时质量控制。通过应用持续学习，我们减少了灾难性遗忘的影响，并提供了一种高效有效的解决方案。

## 🔬 方法详解

论文提出了一种面向工业物联网的边缘计算架构，核心是集成增量学习方法。整体框架包括边缘设备层、数据处理层和学习模块，其中关键技术创新在于将增量学习算法适配到资源受限的边缘环境，以处理动态流入的数据流。与现有方法的主要区别在于，它专门针对工业场景设计，强调实时性和低延迟，而非依赖集中式云处理，从而更有效地应对灾难性遗忘问题，并优化计算资源使用。

## 📊 实验亮点

实验表明，该方法在制造系统实时质量控制任务中有效减少了灾难性遗忘，相比传统方法提升了学习效率和适应性，具体性能提升未知，但强调了在边缘设备上的可行性和效果。

## 🎯 应用场景

该研究主要应用于工业制造领域的实时质量控制，例如生产线上的缺陷检测和过程监控。潜在价值包括提升生产效率、减少停机时间，并支持智能工厂的自动化决策，为工业物联网提供可扩展的边缘智能解决方案。

## 📄 摘要（原文）

> The exponential growth of Internet-connected devices has presented challenges to traditional centralized computing systems due to latency and bandwidth limitations. Edge computing has evolved to address these difficulties by bringing computations closer to the data source. Additionally, traditional machine learning algorithms are not suitable for edge-computing systems, where data usually arrives in a dynamic and continual way. However, incremental learning offers a good solution for these settings. We introduce a new approach that applies the incremental learning philosophy within an edge-computing scenario for the industrial sector with a specific purpose: real time quality control in a manufacturing system. Applying continual learning we reduce the impact of catastrophic forgetting and provide an efficient and effective solution.

