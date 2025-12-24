---
layout: default
title: "Table-r1: Self-supervised and Reinforcement Learning for Program-based Table Reasoning in Small Language Models"
---

# Table-r1: Self-supervised and Reinforcement Learning for Program-based Table Reasoning in Small Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06137" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06137v1</a>
  <a href="https://arxiv.org/pdf/2506.06137.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06137v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06137v1', 'Table-r1: Self-supervised and Reinforcement Learning for Program-based Table Reasoning in Small Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rihui Jin, Zheyu Xin, Xing Xie, Zuoyi Li, Guilin Qi, Yongrui Chen, Xinbang Dai, Tongtong Wu, Gholamreza Haffari

**分类**: cs.LG, cs.CL

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出Table-r1以解决小语言模型的表格推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `表格推理` `小语言模型` `自监督学习` `程序化推理` `策略优化` `机器学习` `数据分析`

## 📋 核心要点

1. 小语言模型在表格推理中面临布局异质性和推理不一致性等挑战，限制了其性能。
2. 提出Table-r1，采用两阶段程序化表格推理方法，结合自监督学习和策略优化技术。
3. 实验结果显示，Table-r1在四个基准测试中超越所有SLM方法，准确率提升至少15%。

## 📝 摘要（中文）

表格推理（TR）需要对半结构化的表格数据进行结构化推理，尤其对于小语言模型（SLMs）如LLaMA-8B而言，因其能力有限而面临挑战。为缩小这一差距，本文探索了一种基于程序的表格推理（P-TR），通过生成可执行程序来克服文本基础表格推理（T-TR）的关键限制。为此，提出了Table-r1，一种针对SLMs的两阶段P-TR方法。第一阶段引入了一种创新的自监督学习任务——布局转换推理，以改善从程序视角的表格布局泛化。第二阶段采用了一种混合范式的群体相对策略优化，增强P-TR的一致性，同时在需要时动态回退到T-TR。实验结果表明，Table-r1在四个TR基准测试中超越了所有基于SLM的方法，在所有数据集上相较于基础模型（LLaMA-8B）至少提高了15%的准确率，并达到了与LLMs竞争的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决小语言模型在表格推理中的局限性，特别是面对表格布局异质性和推理一致性不足的问题。现有方法在处理数值推理时表现不佳，难以适应多样化的表格结构。

**核心思路**：提出基于程序的表格推理（P-TR），通过生成可执行程序来进行推理，克服文本基础推理的局限性。通过自监督学习和策略优化相结合，提升小语言模型的推理能力和一致性。

**技术框架**：Table-r1的整体架构分为两个阶段：第一阶段为布局转换推理，通过自监督学习提升模型对表格布局的泛化能力；第二阶段为混合范式的群体相对策略优化，增强推理的一致性，并在必要时回退到传统的文本基础推理。

**关键创新**：最重要的创新点在于引入自监督学习任务来改善表格布局的泛化能力，以及混合范式的策略优化方法，这与现有方法的单一推理方式形成鲜明对比。

**关键设计**：在自监督学习任务中，设计了特定的损失函数以优化布局转换的效果；在策略优化阶段，采用了动态回退机制，确保在复杂情况下仍能保持推理的准确性。

## 📊 实验亮点

Table-r1在四个表格推理基准测试中表现优异，超越所有基于小语言模型的方法，准确率较基础模型LLaMA-8B提升至少15%，并且在性能上与大型语言模型相竞争，展示了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括数据分析、智能问答系统和自动化报告生成等。通过提升小语言模型在表格推理方面的能力，能够更好地处理实际应用中的复杂数据，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Table reasoning (TR) requires structured reasoning over semi-structured tabular data and remains challenging, particularly for small language models (SLMs, e.g., LLaMA-8B) due to their limited capacity compared to large LMs (LLMs, e.g., GPT-4o). To narrow this gap, we explore program-based TR (P-TR), which circumvents key limitations of text-based TR (T-TR), notably in numerical reasoning, by generating executable programs. However, applying P-TR to SLMs introduces two challenges: (i) vulnerability to heterogeneity in table layouts, and (ii) inconsistency in reasoning due to limited code generation capability. We propose Table-r1, a two-stage P-TR method designed for SLMs. Stage 1 introduces an innovative self-supervised learning task, Layout Transformation Inference, to improve tabular layout generalization from a programmatic view. Stage 2 adopts a mix-paradigm variant of Group Relative Policy Optimization, enhancing P-TR consistency while allowing dynamic fallback to T-TR when needed. Experiments on four TR benchmarks demonstrate that Table-r1 outperforms all SLM-based methods, achieving at least a 15% accuracy improvement over the base model (LLaMA-8B) across all datasets and reaching performance competitive with LLMs.

