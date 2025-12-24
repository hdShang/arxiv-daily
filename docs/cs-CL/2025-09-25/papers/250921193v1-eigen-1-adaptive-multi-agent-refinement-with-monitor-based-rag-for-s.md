---
layout: default
title: "Eigen-1: Adaptive Multi-Agent Refinement with Monitor-Based RAG for Scientific Reasoning"
---

# Eigen-1: Adaptive Multi-Agent Refinement with Monitor-Based RAG for Scientific Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21193" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21193v1</a>
  <a href="https://arxiv.org/pdf/2509.21193.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21193v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21193v1', 'Eigen-1: Adaptive Multi-Agent Refinement with Monitor-Based RAG for Scientific Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangru Tang, Wanghan Xu, Yujie Wang, Zijie Guo, Daniel Shao, Jiapeng Chen, Cixuan Zhang, Ziyi Wang, Lixin Zhang, Guancheng Wan, Wenlong Zhang, Lei Bai, Zhenfei Yin, Philip Torr, Hanrui Wang, Di Jin

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-25

**🔗 代码/项目**: [GITHUB](https://github.com/tangxiangru/Eigen-1)

---

## 💡 一句话要点

**Eigen-1：基于Monitor的RAG自适应多智能体精炼，用于科学推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `科学推理` `多智能体系统` `检索增强生成` `知识整合`

## 📋 核心要点

1. 现有方法在科学推理中，显式检索引入额外开销，多智能体方案平均化导致强解被稀释。
2. 提出Eigen-1框架，结合隐式检索和结构化协作，通过Monitor进行token级知识集成，并进行分层精炼。
3. 在HLE Bio/Chem Gold上达到48.3%准确率，显著超越现有模型，同时降低token使用量和agent步骤。

## 📝 摘要（中文）

大型语言模型（LLMs）在科学推理方面取得了显著进展，但仍存在两大瓶颈。首先，显式检索割裂了推理过程，引入了额外的token和步骤的“工具税”。其次，多智能体管道通常通过平均所有候选方案来稀释强大的解决方案。本文提出了一个统一的框架，结合了隐式检索和结构化协作。该框架的核心是一个基于Monitor的检索模块，它在token级别运行，以最小的干扰将外部知识集成到推理中。在此基础上，分层解决方案精炼（HSR）迭代地将每个候选方案指定为一个锚点，由其同伴进行修复，而质量感知迭代推理（QAIR）则根据解决方案的质量调整精炼过程。在Humanity's Last Exam (HLE) Bio/Chem Gold数据集上，该框架达到了48.3%的准确率，是迄今为止报告的最高水平，超过了最强的agent基线13.4个百分点，并领先于前沿LLM高达18.1个百分点，同时减少了53.5%的token使用量和43.7%的agent步骤。在SuperGPQA和TRQA上的结果证实了跨领域的鲁棒性。误差分析表明，推理失败和知识差距在超过85%的情况下同时发生，而多样性分析揭示了一个明确的二分法：检索任务受益于解决方案的多样性，而推理任务则倾向于共识。这些发现共同证明了隐式增强和结构化精炼如何克服显式工具使用和统一聚合的低效率。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在进行科学推理时，依赖于显式的检索增强，这导致了额外的计算开销（“工具税”），并且多智能体系统在融合多个候选答案时，容易平均化，从而削弱了最优解。因此，如何高效地利用外部知识，并有效地整合多智能体系统的输出，是亟待解决的问题。

**核心思路**：Eigen-1的核心思路是结合隐式检索和结构化协作。隐式检索通过Monitor模块在token级别集成外部知识，减少了显式检索带来的额外开销。结构化协作则通过分层解决方案精炼（HSR）和质量感知迭代推理（QAIR）来优化多智能体系统的输出，避免了简单平均导致的性能下降。

**技术框架**：Eigen-1框架主要包含以下几个模块：1) **Monitor-based Retrieval Module**: 在token级别进行知识检索，将外部知识融入到LLM的推理过程中。2) **Hierarchical Solution Refinement (HSR)**: 迭代地将每个候选方案指定为锚点，并由其他智能体进行修复，从而提升整体解决方案的质量。3) **Quality-Aware Iterative Reasoning (QAIR)**: 根据解决方案的质量自适应地调整精炼过程，使得高质量的解决方案能够得到进一步的优化。

**关键创新**：Eigen-1的关键创新在于其隐式检索和结构化协作的结合。与传统的显式检索方法不同，Eigen-1通过Monitor模块在token级别进行知识集成，避免了额外的计算开销。同时，HSR和QAIR的设计使得多智能体系统能够更有效地协同工作，避免了简单平均导致的性能下降。

**关键设计**：Monitor模块的具体实现细节（例如，如何选择合适的外部知识源，如何将外部知识融入到LLM的推理过程中）以及HSR和QAIR的具体算法（例如，如何选择锚点，如何评估解决方案的质量，如何调整精炼过程）在论文中进行了详细的描述。这些设计细节对于Eigen-1的性能至关重要，但具体参数设置和损失函数等细节需要参考论文原文。

## 📊 实验亮点

Eigen-1在Humanity's Last Exam (HLE) Bio/Chem Gold数据集上取得了48.3%的准确率，是目前报道的最高水平，超过了最强的agent基线13.4个百分点，领先于前沿LLM高达18.1个百分点。同时，该框架还减少了53.5%的token使用量和43.7%的agent步骤。在SuperGPQA和TRQA数据集上的结果也验证了其跨领域的鲁棒性。

## 🎯 应用场景

Eigen-1框架可应用于需要复杂推理和知识整合的科学研究领域，例如生物、化学、医学等。该框架能够提升LLM在这些领域的推理能力，辅助科研人员进行问题求解和知识发现，加速科研进程。未来，该框架还可扩展到其他需要知识增强的领域，如金融分析、法律咨询等。

## 📄 摘要（原文）

> Large language models (LLMs) have recently shown strong progress on scientific reasoning, yet two major bottlenecks remain. First, explicit retrieval fragments reasoning, imposing a hidden "tool tax" of extra tokens and steps. Second, multi-agent pipelines often dilute strong solutions by averaging across all candidates. We address these challenges with a unified framework that combines implicit retrieval and structured collaboration. At its foundation, a Monitor-based retrieval module operates at the token level, integrating external knowledge with minimal disruption to reasoning. On top of this substrate, Hierarchical Solution Refinement (HSR) iteratively designates each candidate as an anchor to be repaired by its peers, while Quality-Aware Iterative Reasoning (QAIR) adapts refinement to solution quality. On Humanity's Last Exam (HLE) Bio/Chem Gold, our framework achieves 48.3\% accuracy -- the highest reported to date, surpassing the strongest agent baseline by 13.4 points and leading frontier LLMs by up to 18.1 points, while simultaneously reducing token usage by 53.5\% and agent steps by 43.7\%. Results on SuperGPQA and TRQA confirm robustness across domains. Error analysis shows that reasoning failures and knowledge gaps co-occur in over 85\% of cases, while diversity analysis reveals a clear dichotomy: retrieval tasks benefit from solution variety, whereas reasoning tasks favor consensus. Together, these findings demonstrate how implicit augmentation and structured refinement overcome the inefficiencies of explicit tool use and uniform aggregation. Code is available at: https://github.com/tangxiangru/Eigen-1.

