---
layout: default
title: Differentially Private Knowledge Distillation via Synthetic Text Generation
---

# Differentially Private Knowledge Distillation via Synthetic Text Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2403.00932" class="toolbar-btn" target="_blank">📄 arXiv: 2403.00932</a>
  <a href="https://arxiv.org/pdf/2403.00932.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2403.00932" onclick="toggleFavorite(this, '2403.00932', 'Differentially Private Knowledge Distillation via Synthetic Text Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: James Flemings, Murali Annavaram

**分类**: cs.LG, cs.CL, cs.CR

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出DistilDP以解决差分隐私与知识蒸馏的平衡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `差分隐私` `知识蒸馏` `大型语言模型` `合成数据` `模型压缩` `隐私保护` `自然语言处理`

## 📋 核心要点

1. 现有方法在实现差分隐私和模型压缩时，往往面临效用损失的权衡，且同时应用两者可能导致更大的效用下降。
2. 本文提出DistilDP算法，通过合成数据生成和教师模型的输出分布，进行知识蒸馏，从而有效提升模型性能。
3. 实验结果显示，DistilDP在Big Patent数据集上相较于现有基线至少提升了9.0 PPL，展现出强大的隐私保护能力。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个下游任务中表现出色，但数据隐私的日益紧迫性要求在私有数据上使用差分隐私（DP）进行训练。同时，LLMs参数规模的指数增长也需要在资源受限或延迟敏感的应用中进行模型压缩。差分隐私和模型压缩通常需要在效用损失上进行权衡，且同时应用两者可能会加剧效用下降。为此，本文提出了一种新颖的差分隐私知识蒸馏算法DistilDP，该算法利用由差分隐私教师LLM生成的合成数据进行知识传递。实验结果表明，DistilDP在Big Patent数据集上相较于现有基线显著提高了效用，隐私参数为ε=2时至少提升了9.0 PPL。这些结果推动了自回归LLMs的隐私保护压缩进程。

## 🔬 方法详解

**问题定义**：本文旨在解决在私有数据上训练大型语言模型时，如何在保证差分隐私的同时进行有效的模型压缩。现有方法在同时应用差分隐私和知识蒸馏时，往往导致效用显著下降。

**核心思路**：DistilDP算法通过利用差分隐私教师模型生成的合成数据，进行知识的双重传递：一方面通过合成数据的硬标签，另一方面通过教师模型在合成数据上的输出分布（软标签），从而提升学生模型的性能。

**技术框架**：DistilDP的整体架构包括两个主要模块：教师模型生成合成数据和学生模型进行知识蒸馏。教师模型首先生成合成数据，然后学生模型通过学习硬标签和软标签来进行知识的吸收和转移。

**关键创新**：DistilDP的核心创新在于结合了差分隐私和知识蒸馏的思想，通过合成数据的生成和标签的双重利用，显著提升了模型的效用，克服了传统方法的局限性。

**关键设计**：在设计中，教师和学生模型的架构相似，以便于对隐藏表示进行对齐。此外，隐私参数ε的设置为2，确保了在保证隐私的前提下，模型的性能得以提升。实验中使用的损失函数和训练策略也经过精心设计，以最大化知识的转移效果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2403.00932/figures/dpkd_overview.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，DistilDP在Big Patent数据集上相较于现有基线至少提升了9.0 PPL，展现出强大的隐私保护能力，隐私参数设置为ε=2，证明了其在隐私保护下的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括需要保护用户隐私的自然语言处理任务，如医疗记录分析、金融数据处理等。通过在保证隐私的同时提升模型性能，DistilDP为实际应用提供了新的解决方案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language models (LLMs) are achieving state-of-the-art performance in many different downstream tasks. However, the increasing urgency of data privacy puts pressure on practitioners to train LLMs with Differential Privacy (DP) on private data. Concurrently, the exponential growth in parameter size of LLMs necessitates model compression before deployment of LLMs on resource-constrained devices or latency-sensitive applications. Differential privacy and model compression generally must trade off utility loss to achieve their objectives. Moreover, simultaneously applying both schemes can compound the utility degradation. To this end, we propose DistilDP: a novel differentially private knowledge distillation algorithm that exploits synthetic data generated by a differentially private teacher LLM. The knowledge of a teacher LLM is transferred onto the student in two ways: one way from the synthetic data itself -- the hard labels, and the other way by the output distribution of the teacher evaluated on the synthetic data -- the soft labels. Furthermore, if the teacher and student share a similar architectural structure, we can further distill knowledge by aligning the hidden representations between both. Our experimental results demonstrate that DistilDP can substantially improve the utility over existing baselines, at least $9.0$ PPL on the Big Patent dataset, with strong privacy parameters, $\epsilon=2$. These promising results progress privacy-preserving compression of autoregressive LLMs. Our code can be accessed here:this https URL.

