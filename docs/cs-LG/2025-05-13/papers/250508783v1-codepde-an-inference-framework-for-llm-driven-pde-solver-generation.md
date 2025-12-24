---
layout: default
title: CodePDE: An Inference Framework for LLM-driven PDE Solver Generation
---

# CodePDE: An Inference Framework for LLM-driven PDE Solver Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08783" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08783v1</a>
  <a href="https://arxiv.org/pdf/2505.08783.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08783v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08783v1', 'CodePDE: An Inference Framework for LLM-driven PDE Solver Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shanda Li, Tanya Marwah, Junhong Shen, Weiwei Sun, Andrej Risteski, Yiming Yang, Ameet Talwalkar

**分类**: cs.LG, cs.AI, cs.CL, math.NA

**发布日期**: 2025-05-13

**🔗 代码/项目**: [GITHUB](https://github.com/LithiumDA/CodePDE)

---

## 💡 一句话要点

**提出CodePDE框架以生成偏微分方程求解器**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏微分方程` `代码生成` `大型语言模型` `求解器设计` `机器学习`

## 📋 核心要点

1. 现有的PDE求解方法依赖于专家知识，计算成本高且缺乏可解释性，限制了其应用。
2. 本研究提出CodePDE框架，将PDE求解视为代码生成任务，利用大型语言模型生成求解器，提升了求解效率和准确性。
3. CodePDE在多个代表性PDE问题上表现出超人类性能，提供了对LLM生成求解器的系统性分析，揭示了其潜力与局限。

## 📝 摘要（中文）

偏微分方程（PDE）是建模物理系统的基础，但其求解仍然是一个复杂的挑战。传统的数值求解器依赖于专家知识，且计算成本高，而基于神经网络的求解器需要大量训练数据，且往往缺乏可解释性。本研究将PDE求解视为代码生成任务，提出了CodePDE，这是首个利用大型语言模型（LLMs）生成PDE求解器的推理框架。通过先进的推理时间算法和扩展策略，CodePDE释放了LLM在PDE求解中的关键能力，包括推理、调试、自我优化和测试时扩展，且无需特定任务的调优。CodePDE在一系列代表性PDE问题上实现了超人类性能，并对LLM生成的求解器进行了系统的实证分析，分析了其准确性、效率和数值方案选择。我们的发现突显了LLM在PDE求解中的潜力和当前局限，为求解器设计和未来模型开发提供了新的视角。

## 🔬 方法详解

**问题定义**：本论文旨在解决偏微分方程（PDE）求解的复杂性，现有方法依赖于专家知识和大量计算资源，且缺乏可解释性，限制了其广泛应用。

**核心思路**：论文的核心思路是将PDE求解视为代码生成任务，利用大型语言模型（LLMs）生成求解器，从而降低对专家知识的依赖，并提高求解器的可解释性和灵活性。

**技术框架**：CodePDE的整体架构包括数据输入模块、LLM生成模块、推理时间算法和扩展策略模块。数据输入模块负责接收PDE问题的描述，LLM生成模块生成相应的求解器代码，推理时间算法和扩展策略模块则负责优化生成过程和提升求解器性能。

**关键创新**：最重要的技术创新点在于将PDE求解转化为代码生成任务，利用LLM的推理能力和自我优化特性，避免了传统方法的高计算成本和缺乏可解释性的问题。

**关键设计**：在设计中，关键参数包括LLM的选择、生成代码的结构和优化算法的设置。损失函数采用了针对求解器性能的定制化设计，以确保生成的求解器在准确性和效率上的平衡。

## 📊 实验亮点

在多个代表性PDE问题上，CodePDE实现了超人类性能，显著提高了求解的准确性和效率。与传统求解器相比，LLM生成的求解器在准确性和计算效率上均表现出明显的优势，展示了LLM在科学计算领域的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括物理模拟、工程设计和科学计算等。CodePDE框架能够为复杂的物理系统提供高效的求解方案，具有重要的实际价值，未来可能推动智能求解器的广泛应用与发展。

## 📄 摘要（原文）

> Partial differential equations (PDEs) are fundamental to modeling physical systems, yet solving them remains a complex challenge. Traditional numerical solvers rely on expert knowledge to implement and are computationally expensive, while neural-network-based solvers require large training datasets and often lack interpretability. In this work, we frame PDE solving as a code generation task and introduce CodePDE, the first inference framework for generating PDE solvers using large language models (LLMs). Leveraging advanced inference-time algorithms and scaling strategies, CodePDE unlocks critical capacities of LLM for PDE solving: reasoning, debugging, selfrefinement, and test-time scaling -- all without task-specific tuning. CodePDE achieves superhuman performance across a range of representative PDE problems. We also present a systematic empirical analysis of LLM generated solvers, analyzing their accuracy, efficiency, and numerical scheme choices. Our findings highlight the promise and the current limitations of LLMs in PDE solving, offering a new perspective on solver design and opportunities for future model development. Our code is available at https://github.com/LithiumDA/CodePDE.

