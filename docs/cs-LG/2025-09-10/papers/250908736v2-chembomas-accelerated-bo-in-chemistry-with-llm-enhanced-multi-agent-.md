---
layout: default
title: "ChemBOMAS: Accelerated BO in Chemistry with LLM-Enhanced Multi-Agent System"
---

# ChemBOMAS: Accelerated BO in Chemistry with LLM-Enhanced Multi-Agent System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08736" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08736v2</a>
  <a href="https://arxiv.org/pdf/2509.08736.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08736v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08736v2', 'ChemBOMAS: Accelerated BO in Chemistry with LLM-Enhanced Multi-Agent System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dong Han, Zhehong Ai, Pengxiang Cai, Shanya Lu, Jianpeng Chen, Zihao Ye, Shuzhou Sun, Ben Gao, Lingli Ge, Weida Wang, Xiangxin Zhou, Xihui Liu, Mao Su, Wanli Ouyang, Lei Bai, Dongzhan Zhou, Tao Xu, Yuqiang Li, Shufei Zhang

**分类**: cs.LG

**发布日期**: 2025-09-10 (更新: 2025-11-10)

---

## 💡 一句话要点

**ChemBOMAS：利用LLM增强的多智能体系统加速化学领域的贝叶斯优化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `贝叶斯优化` `大型语言模型` `多智能体系统` `化学信息学` `实验设计` `数据增强` `知识驱动`

## 📋 核心要点

1. 化学领域的贝叶斯优化面临数据稀疏和搜索空间巨大的挑战，限制了其效率。
2. ChemBOMAS利用LLM生成伪数据初始化优化，并结合检索增强生成划分搜索空间，提升BO性能。
3. 实验表明，ChemBOMAS在多个基准测试中达到SOTA，优化效率提升高达5倍。

## 📝 摘要（中文）

贝叶斯优化(BO)是化学科学发现的强大工具，但其效率常受限于稀疏的实验数据和巨大的搜索空间。本文提出了ChemBOMAS：一个大型语言模型(LLM)增强的多智能体系统，通过协同的数据驱动和知识驱动策略来加速BO。首先，数据驱动策略涉及一个80亿参数规模的LLM回归器，仅用1%的标记样本进行微调，以生成伪数据，从而稳健地初始化优化过程。其次，知识驱动策略采用混合检索增强生成方法，引导LLM划分搜索空间，同时减轻LLM的幻觉问题。然后，上限置信区间算法识别已建立分区中的高潜力子空间。在LLM精炼的子空间中，并在LLM生成数据的支持下，BO实现了有效性和效率的提高。在多个科学基准上的全面评估表明，ChemBOMAS达到了新的最先进水平，与基线方法相比，优化效率提高了高达5倍。

## 🔬 方法详解

**问题定义**：贝叶斯优化在化学领域面临数据稀疏和搜索空间巨大的问题。传统的贝叶斯优化方法在数据量不足的情况下，难以有效地探索整个搜索空间，导致优化效率低下，难以找到全局最优解。现有方法难以充分利用领域知识来指导搜索，容易陷入局部最优。

**核心思路**：ChemBOMAS的核心思路是利用大型语言模型（LLM）的强大能力来增强贝叶斯优化过程。通过LLM生成伪数据来解决数据稀疏问题，并利用LLM的知识推理能力来划分搜索空间，从而引导贝叶斯优化更有效地探索有潜力的区域。这种数据驱动和知识驱动相结合的策略旨在提高贝叶斯优化的效率和效果。

**技术框架**：ChemBOMAS包含两个主要模块：数据驱动模块和知识驱动模块。数据驱动模块使用一个在少量标记数据上微调的LLM回归器生成伪数据，用于初始化贝叶斯优化过程。知识驱动模块采用混合检索增强生成方法，利用LLM划分搜索空间，并使用上限置信区间算法识别高潜力子空间。最终，在LLM精炼的子空间和LLM生成数据的支持下，进行贝叶斯优化。

**关键创新**：ChemBOMAS的关键创新在于将LLM与贝叶斯优化相结合，利用LLM的数据生成和知识推理能力来克服传统贝叶斯优化在化学领域面临的挑战。具体来说，利用LLM生成伪数据缓解了数据稀疏问题，利用LLM划分搜索空间并减轻幻觉问题，从而更有效地探索搜索空间。这种LLM增强的贝叶斯优化方法与现有方法有本质区别。

**关键设计**：数据驱动模块中，LLM回归器采用80亿参数规模，并在1%的标记样本上进行微调。知识驱动模块采用混合检索增强生成方法，具体实现细节未知。上限置信区间算法的具体参数设置未知。损失函数和网络结构等技术细节在论文中没有详细描述。

## 📊 实验亮点

ChemBOMAS在多个科学基准测试中表现出色，达到了新的最先进水平。与基线方法相比，ChemBOMAS的优化效率提高了高达5倍。这些实验结果表明，ChemBOMAS能够有效地解决化学领域贝叶斯优化面临的数据稀疏和搜索空间巨大的问题，显著提升优化效率。

## 🎯 应用场景

ChemBOMAS可应用于化学、材料科学等领域的实验设计与优化，例如新材料发现、药物设计、催化剂优化等。通过加速优化过程，ChemBOMAS能够降低实验成本，缩短研发周期，加速科学发现。该方法有望推动相关领域的研究进展，并为实际应用带来显著的经济和社会效益。

## 📄 摘要（原文）

> Bayesian optimization (BO) is a powerful tool for scientific discovery in chemistry, yet its efficiency is often hampered by the sparse experimental data and vast search space. Here, we introduce ChemBOMAS: a large language model (LLM)-enhanced multi-agent system that accelerates BO through synergistic data- and knowledge-driven strategies. Firstly, the data-driven strategy involves an 8B-scale LLM regressor fine-tuned on a mere 1% labeled samples for pseudo-data generation, robustly initializing the optimization process. Secondly, the knowledge-driven strategy employs a hybrid Retrieval-Augmented Generation approach to guide LLM in dividing the search space while mitigating LLM hallucinations. An Upper Confidence Bound algorithm then identifies high-potential subspaces within this established partition. Across the LLM-refined subspaces and supported by LLM-generated data, BO achieves the improvement of effectiveness and efficiency. Comprehensive evaluations across multiple scientific benchmarks demonstrate that ChemBOMAS set a new state-of-the-art, accelerating optimization efficiency by up to 5-fold compared to baseline methods.

