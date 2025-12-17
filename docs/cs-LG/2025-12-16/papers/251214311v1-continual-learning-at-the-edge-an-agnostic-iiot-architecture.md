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

**提出一种面向工业边缘计算的持续学习方法，用于实时质量控制，减少灾难性遗忘影响。**

**关键词**: `边缘计算` `持续学习` `工业物联网` `增量学习` `实时质量控制` `灾难性遗忘` `智能制造`

## 📋 核心要点

1. 传统集中式计算面临延迟和带宽限制，边缘计算成为解决方案，但传统机器学习算法不适应动态数据流。
2. 论文提出在工业边缘计算场景中应用增量学习，实现实时质量控制，减少灾难性遗忘。
3. 该方法提供高效解决方案，提升边缘系统的适应性和性能，具体实验结果未知。

## 📝 摘要（中文）

互联网连接设备的指数级增长给传统集中式计算系统带来了延迟和带宽限制的挑战。边缘计算通过将计算更靠近数据源来解决这些困难。此外，传统机器学习算法不适合边缘计算系统，因为数据通常以动态和持续的方式到达。然而，增量学习为这些场景提供了良好的解决方案。我们引入了一种新方法，将增量学习理念应用于工业领域的边缘计算场景，具体目的是在制造系统中实现实时质量控制。通过应用持续学习，我们减少了灾难性遗忘的影响，并提供了一种高效且有效的解决方案。

## 🔬 方法详解

论文提出一种面向工业物联网的边缘计算架构，核心是应用持续学习方法。整体框架将增量学习集成到边缘节点，处理动态数据流。关键技术创新在于将持续学习理念专门化到工业质量控制场景，优化模型更新策略以减少灾难性遗忘。与现有方法的主要区别在于结合边缘计算和持续学习，针对工业实时需求设计，而非通用机器学习框架。

## 📊 实验亮点

论文通过应用持续学习，有效减少了灾难性遗忘的影响，提供了边缘计算场景下的高效解决方案。具体性能提升未知，但强调了方法在实时工业应用中的适应性和有效性。

## 🎯 应用场景

该研究主要应用于工业制造领域的实时质量控制，如生产线监测、缺陷检测等。潜在价值包括提升生产效率、降低延迟，并适应动态环境变化，推动工业自动化和智能化。

## 📄 摘要（原文）

> The exponential growth of Internet-connected devices has presented challenges to traditional centralized computing systems due to latency and bandwidth limitations. Edge computing has evolved to address these difficulties by bringing computations closer to the data source. Additionally, traditional machine learning algorithms are not suitable for edge-computing systems, where data usually arrives in a dynamic and continual way. However, incremental learning offers a good solution for these settings. We introduce a new approach that applies the incremental learning philosophy within an edge-computing scenario for the industrial sector with a specific purpose: real time quality control in a manufacturing system. Applying continual learning we reduce the impact of catastrophic forgetting and provide an efficient and effective solution.

