---
layout: default
title: Reason2Decide: Rationale-Driven Multi-Task Learning
---

# Reason2Decide: Rationale-Driven Multi-Task Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20074" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20074v1</a>
  <a href="https://arxiv.org/pdf/2512.20074.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20074v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20074v1', 'Reason2Decide: Rationale-Driven Multi-Task Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: H M Quamran Hasan, Housam Khalifa Bashier, Jiayi Dai, Mi-Young Kim, Randy Goebel

**分类**: cs.AI, cs.CL

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**Reason2Decide：一种基于理由驱动的多任务学习框架，提升临床决策支持系统的预测精度和解释一致性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `临床决策支持` `多任务学习` `理由生成` `可解释性` `暴露偏差`

## 📋 核心要点

1. 现有临床决策支持系统难以兼顾预测精度和解释一致性，存在暴露偏差导致解释与预测不符。
2. Reason2Decide采用两阶段训练，先生成理由，再联合训练预测和理由，利用scheduled sampling缓解暴露偏差。
3. 实验表明，Reason2Decide在医疗数据集上优于其他微调基线，且对不同来源的理由具有鲁棒性，模型规模更小。

## 📝 摘要（中文）

大型语言模型（LLM）广泛应用，但临床决策支持系统面临一个关键挑战：在实现高预测精度的同时，生成与预测结果一致的解释。现有方法存在暴露偏差，导致解释错位。我们提出了Reason2Decide，一个两阶段训练框架，解决自解释中的关键挑战，包括暴露偏差和任务分离。在第一阶段，模型训练生成理由；在第二阶段，模型联合训练标签预测和理由生成，应用scheduled sampling逐步从依赖真实标签过渡到依赖模型预测。我们在三个医疗数据集上评估Reason2Decide，包括一个专有的分诊数据集和公开的生物医学问答数据集。在不同模型规模下，Reason2Decide在预测（F1）和理由保真度（BERTScore、BLEU、LLM-as-a-Judge）方面优于其他微调基线和一些零样本LLM。在分诊任务中，Reason2Decide对LLM生成、护士撰写和护士后处理的理由具有鲁棒性。实验表明，仅在第一阶段使用LLM生成的理由，Reason2Decide就优于其他微调变体，表明LLM生成的理由适合预训练模型，减少对人工标注的依赖。值得注意的是，Reason2Decide以比现有基础模型小40倍的模型实现了这些改进，使临床推理更易于在资源受限的部署中使用，同时仍提供可解释的决策支持。

## 🔬 方法详解

**问题定义**：临床决策支持系统需要高预测精度和与预测一致的解释，但现有方法存在暴露偏差，即训练时依赖真实标签，推理时依赖模型预测，导致解释与预测不一致。此外，理由生成和标签预测两个任务耦合度不高，直接联合训练效果不佳。

**核心思路**：Reason2Decide的核心思路是将理由生成和标签预测解耦，分阶段训练。首先训练模型生成高质量的理由，然后利用生成的理由辅助标签预测，并使用scheduled sampling缓解暴露偏差。这样可以提高模型的预测精度和解释一致性。

**技术框架**：Reason2Decide是一个两阶段训练框架。第一阶段，使用LLM生成的理由数据训练模型，使其具备生成合理理由的能力。第二阶段，联合训练标签预测和理由生成任务，使用scheduled sampling策略，逐渐从依赖真实标签过渡到依赖模型预测，从而缓解暴露偏差。整体流程是先预训练理由生成，再微调预测和理由生成。

**关键创新**：Reason2Decide的关键创新在于两阶段训练框架和scheduled sampling策略。两阶段训练解耦了理由生成和标签预测任务，提高了训练效率和效果。Scheduled sampling缓解了暴露偏差，提高了模型在推理时的性能。此外，该方法可以使用LLM生成的理由进行预训练，减少了对人工标注数据的依赖。

**关键设计**：第一阶段使用交叉熵损失函数训练理由生成模型。第二阶段，使用交叉熵损失函数训练标签预测模型，并使用交叉熵损失函数或BERTScore等指标作为理由生成模型的损失函数。Scheduled sampling策略通过调整使用真实标签的概率，逐步过渡到使用模型预测，具体概率由一个schedule函数控制。模型结构可以是Transformer等序列到序列模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20074v1/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Reason2Decide在三个医疗数据集上进行了评估，包括一个专有的分诊数据集和公开的生物医学问答数据集。实验结果表明，Reason2Decide在预测（F1）和理由保真度（BERTScore、BLEU、LLM-as-a-Judge）方面优于其他微调基线和一些零样本LLM。在分诊任务中，Reason2Decide对LLM生成、护士撰写和护士后处理的理由具有鲁棒性。使用LLM生成的理由进行预训练，Reason2Decide仍然优于其他微调变体。

## 🎯 应用场景

Reason2Decide可应用于各种临床决策支持系统，例如疾病诊断、治疗方案选择、风险评估等。该方法能够提供高精度的预测结果，并生成与预测一致的解释，有助于医生理解模型的决策过程，提高信任度，并辅助临床决策。此外，该方法可以使用LLM生成的理由进行预训练，降低了对人工标注数据的依赖，具有广泛的应用前景。

## 📄 摘要（原文）

> Despite the wide adoption of Large Language Models (LLM)s, clinical decision support systems face a critical challenge: achieving high predictive accuracy while generating explanations aligned with the predictions. Current approaches suffer from exposure bias leading to misaligned explanations. We propose Reason2Decide, a two-stage training framework that addresses key challenges in self-rationalization, including exposure bias and task separation. In Stage-1, our model is trained on rationale generation, while in Stage-2, we jointly train on label prediction and rationale generation, applying scheduled sampling to gradually transition from conditioning on gold labels to model predictions. We evaluate Reason2Decide on three medical datasets, including a proprietary triage dataset and public biomedical QA datasets. Across model sizes, Reason2Decide outperforms other fine-tuning baselines and some zero-shot LLMs in prediction (F1) and rationale fidelity (BERTScore, BLEU, LLM-as-a-Judge). In triage, Reason2Decide is rationale source-robust across LLM-generated, nurse-authored, and nurse-post-processed rationales. In our experiments, while using only LLM-generated rationales in Stage-1, Reason2Decide outperforms other fine-tuning variants. This indicates that LLM-generated rationales are suitable for pretraining models, reducing reliance on human annotations. Remarkably, Reason2Decide achieves these gains with models 40x smaller than contemporary foundation models, making clinical reasoning more accessible for resource-constrained deployments while still providing explainable decision support.

