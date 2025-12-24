---
layout: default
title: "KDH-MLTC: Knowledge Distillation for Healthcare Multi-Label Text Classification"
---

# KDH-MLTC: Knowledge Distillation for Healthcare Multi-Label Text Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07162" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07162v1</a>
  <a href="https://arxiv.org/pdf/2505.07162.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07162v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07162v1', 'KDH-MLTC: Knowledge Distillation for Healthcare Multi-Label Text Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hajar Sakai, Sarah S. Lam

**分类**: cs.CL

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出KDH-MLTC以解决医疗多标签文本分类问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识蒸馏` `医疗文本分类` `多标签分类` `粒子群优化` `模型压缩` `顺序微调` `大型语言模型`

## 📋 核心要点

1. 现有医疗文本分类方法在处理复杂医学术语时，往往面临计算资源不足和准确性不足的挑战。
2. KDH-MLTC通过知识蒸馏和顺序微调，将复杂模型的知识转移到轻量模型，优化计算效率和准确性。
3. 在三个医疗文献数据集上，KDH-MLTC的F1分数达82.70%，显著优于现有方法，尤其在大数据集上表现突出。

## 📝 摘要（中文）

随着医疗文本数据量的增加，亟需高效且准确的分类方法来处理复杂的医学术语。本文提出了医疗多标签文本分类的知识蒸馏框架KDH-MLTC，该框架结合了模型压缩和大型语言模型（LLMs）。通过知识蒸馏和顺序微调，KDH-MLTC有效应对传统医疗多标签文本分类的挑战，并通过粒子群优化（PSO）进行超参数调优。该方法将复杂的教师模型（如BERT）中的知识转移到轻量级学生模型（如DistilBERT），在保留教师学习信息的同时显著降低计算需求。实验结果显示，KDH-MLTC在三个不同规模的医疗文献数据集上表现优异，尤其在最大数据集上达到了82.70%的F1分数，证明了其有效性和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决医疗多标签文本分类中的计算效率和准确性问题。现有方法在处理复杂医学术语时，往往需要大量计算资源，难以满足实际应用需求。

**核心思路**：KDH-MLTC的核心思路是通过知识蒸馏将复杂的教师模型（如BERT）的知识转移到轻量级学生模型（如DistilBERT），并结合顺序微调和粒子群优化，以提高分类效率和准确性。

**技术框架**：KDH-MLTC的整体架构包括知识蒸馏模块、顺序微调模块和超参数优化模块。首先，通过知识蒸馏将教师模型的知识转移到学生模型，然后进行顺序微调，最后利用粒子群优化进行超参数调优，以获得最佳模型配置。

**关键创新**：KDH-MLTC的主要创新在于将知识蒸馏与顺序微调相结合，并通过粒子群优化进行超参数调优。这种方法不仅保留了教师模型的学习信息，还显著降低了计算需求，适用于资源受限的医疗环境。

**关键设计**：在模型设计中，采用了DistilBERT作为学生模型，并通过特定的损失函数来优化知识蒸馏过程。同时，粒子群优化用于寻找最佳的超参数配置，以提高模型的整体性能。实验中还进行了消融研究，以验证各个模块的有效性。

## 📊 实验亮点

在实验中，KDH-MLTC在三个不同规模的医疗文献数据集上表现优异，尤其在最大数据集上达到了82.70%的F1分数，显著高于现有方法。这一结果证明了KDH-MLTC在医疗多标签文本分类中的有效性和鲁棒性，同时也展示了其在资源受限环境中的应用潜力。

## 🎯 应用场景

KDH-MLTC具有广泛的应用潜力，特别是在医疗文本分类领域。其高效的分类能力使其适用于医院、诊所等资源受限的医疗环境，能够帮助医疗专业人员快速、准确地处理大量医疗文献，从而提高医疗决策的效率和准确性。此外，该方法的HIPAA合规性确保了患者数据的安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The increasing volume of healthcare textual data requires computationally efficient, yet highly accurate classification approaches able to handle the nuanced and complex nature of medical terminology. This research presents Knowledge Distillation for Healthcare Multi-Label Text Classification (KDH-MLTC), a framework leveraging model compression and Large Language Models (LLMs). The proposed approach addresses conventional healthcare Multi-Label Text Classification (MLTC) challenges by integrating knowledge distillation and sequential fine-tuning, subsequently optimized through Particle Swarm Optimization (PSO) for hyperparameter tuning. KDH-MLTC transfers knowledge from a more complex teacher LLM (i.e., BERT) to a lighter student LLM (i.e., DistilBERT) through sequential training adapted to MLTC that preserves the teacher's learned information while significantly reducing computational requirements. As a result, the classification is enabled to be conducted locally, making it suitable for healthcare textual data characterized by sensitivity and, therefore, ensuring HIPAA compliance. The experiments conducted on three medical literature datasets of different sizes, sampled from the Hallmark of Cancer (HoC) dataset, demonstrate that KDH-MLTC achieves superior performance compared to existing approaches, particularly for the largest dataset, reaching an F1 score of 82.70%. Additionally, statistical validation and an ablation study are carried out, proving the robustness of KDH-MLTC. Furthermore, the PSO-based hyperparameter optimization process allowed the identification of optimal configurations. The proposed approach contributes to healthcare text classification research, balancing efficiency requirements in resource-constrained healthcare settings with satisfactory accuracy demands.

