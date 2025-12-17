---
layout: default
title: gridfm-datakit-v1: A Python Library for Scalable and Realistic Power Flow and Optimal Power Flow Data Generation
---

# gridfm-datakit-v1: A Python Library for Scalable and Realistic Power Flow and Optimal Power Flow Data Generation

**arXiv**: [2512.14658v1](https://arxiv.org/abs/2512.14658) | [PDF](https://arxiv.org/pdf/2512.14658.pdf)

**作者**: Alban Puech, Matteo Mazzonelli, Celia Cintas, Tamara R. Govindasamy, Mangaliso Mngomezulu, Jonas Weiss, Matteo Baù, Anna Varbella, François Mirallès, Kibaek Kim, Le Xie, Hendrik F. Hamann, Etienne Vos, Thomas Brunschwiler

**分类**: cs.LG, cs.AI, eess.SY, math.OC

**发布日期**: 2025-12-16

**备注**: Main equal contributors: Alban Puech, Matteo Mazzonelli. Other equal contributors: Celia Cintas, Tamara R. Govindasamy, Mangaliso Mngomezulu, Jonas Weiss

**🔗 代码/项目**: [GITHUB](https://github.com/gridfm/gridfm-datakit)

---

## 💡 一句话要点

**提出gridfm-datakit-v1 Python库，以生成可扩展且现实的潮流和最优潮流数据集，解决现有数据生成方法的多样性不足和泛化限制问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `潮流数据生成` `最优潮流数据生成` `机器学习求解器` `电力系统模拟` `数据多样性` `泛化能力` `Python库` `电网优化`

## 📋 核心要点

1. 现有方法缺乏现实随机负荷和拓扑扰动，导致数据集多样性不足，限制了机器学习求解器的训练效果。
2. 通过结合全局负荷缩放、局部噪声和N-k拓扑扰动，生成多样且现实的PF和OPF数据，并支持超出运行限制的样本和变化成本。
3. 库能高效扩展到10,000节点电网，相比现有工具，在数据多样性和泛化能力方面有显著提升。

## 📝 摘要（中文）

我们介绍了gridfm-datakit-v1，这是一个用于生成现实且多样化的潮流（PF）和最优潮流（OPF）数据集的Python库，旨在训练机器学习（ML）求解器。现有数据集和库面临三个主要挑战：（1）缺乏现实的随机负荷和拓扑扰动，限制了场景多样性；（2）PF数据集仅限于OPF可行点，阻碍了ML求解器对违反运行限制（如支路过载或电压违规）情况的泛化；（3）OPF数据集使用固定的发电机成本函数，限制了在不同成本下的泛化能力。gridfm-datakit通过以下方式应对这些挑战：（1）结合来自真实世界配置文件的全局负荷缩放与局部噪声，并支持任意的N-k拓扑扰动，以创建多样且现实的数据集；（2）生成超出运行限制的PF样本；（3）生成具有变化发电机成本的OPF数据。它还高效扩展到大型电网（最多10,000个节点）。提供了与OPFData、OPF-Learn、PGLearn和PF$Δ$的比较。该库可在GitHub上获取，网址为https://github.com/gridfm/gridfm-datakit，遵循Apache 2.0许可，并通过`pip install gridfm-datakit`安装。

## 🔬 方法详解

gridfm-datakit-v1的整体框架是一个基于Python的数据生成库，专注于潮流和最优潮流模拟。关键技术创新点包括：结合真实世界负荷配置文件的全局缩放与局部噪声，以模拟现实负荷变化；支持任意的N-k拓扑扰动，增强数据集的多样性和现实性；生成超出运行限制的PF样本，以训练ML求解器处理违规情况；以及生成具有变化发电机成本的OPF数据，提高成本泛化能力。与现有方法的主要区别在于，它解决了现有库在随机扰动、泛化限制和成本固定方面的不足，提供了更全面和可扩展的数据生成方案。

## 📊 实验亮点

实验表明，gridfm-datakit能生成多样且现实的数据集，扩展到10,000节点电网，相比OPFData等工具，在数据多样性和泛化能力方面有显著改进，支持超出运行限制的样本和变化成本。

## 🎯 应用场景

该研究主要应用于电力系统优化和机器学习领域，可用于训练和评估潮流和最优潮流的ML求解器，支持电网规划、实时控制和能源管理，提升电力系统的效率和可靠性。

## 📄 摘要（原文）

> We introduce gridfm-datakit-v1, a Python library for generating realistic and diverse Power Flow (PF) and Optimal Power Flow (OPF) datasets for training Machine Learning (ML) solvers. Existing datasets and libraries face three main challenges: (1) lack of realistic stochastic load and topology perturbations, limiting scenario diversity; (2) PF datasets are restricted to OPF-feasible points, hindering generalization of ML solvers to cases that violate operating limits (e.g., branch overloads or voltage violations); and (3) OPF datasets use fixed generator cost functions, limiting generalization across varying costs. gridfm-datakit addresses these challenges by: (1) combining global load scaling from real-world profiles with localized noise and supporting arbitrary N-k topology perturbations to create diverse yet realistic datasets; (2) generating PF samples beyond operating limits; and (3) producing OPF data with varying generator costs. It also scales efficiently to large grids (up to 10,000 buses). Comparisons with OPFData, OPF-Learn, PGLearn, and PF$Δ$ are provided. Available on GitHub at https://github.com/gridfm/gridfm-datakit under Apache 2.0 and via `pip install gridfm-datakit`.

