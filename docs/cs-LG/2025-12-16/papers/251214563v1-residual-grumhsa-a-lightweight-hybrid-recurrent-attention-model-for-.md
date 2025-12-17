---
layout: default
title: Residual GRU+MHSA: A Lightweight Hybrid Recurrent Attention Model for Cardiovascular Disease Detection
---

# Residual GRU+MHSA: A Lightweight Hybrid Recurrent Attention Model for Cardiovascular Disease Detection

**arXiv**: [2512.14563v1](https://arxiv.org/abs/2512.14563) | [PDF](https://arxiv.org/pdf/2512.14563.pdf)

**作者**: Tejaswani Dash, Gautam Datla, Anudeep Vurity, Tazeem Ahmad, Mohd Adnan, Saima Rafi, Saisha Patro, Saina Patro

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**备注**: Accepted in IEEE Bigdata 2025- Learning Representations with Limited Supervision

---

## 💡 一句话要点

**提出Residual GRU+MHSA轻量混合循环注意力模型，用于心血管疾病检测，平衡准确性与效率。**

**关键词**: `心血管疾病检测` `轻量深度学习` `残差双向GRU` `多头自注意力` `表格数据建模` `临床风险预测` `混合循环注意力模型` `医疗人工智能`

## 📋 核心要点

1. 核心问题：传统心血管疾病诊断依赖手工特征和专家经验，机器学习方法在噪声和异质临床数据中泛化能力有限。
2. 方法要点：提出轻量混合模型，结合残差双向GRU进行序列建模、通道重加权和多头自注意力池化，以捕获全局上下文。
3. 实验或效果：在UCI心脏病数据集上，模型准确率达0.861，优于经典和深度学习基线，消融研究验证各组件贡献。

## 📝 摘要（中文）

心血管疾病（CVD）是全球主要死因，需要可靠高效的预测工具以支持早期干预。传统诊断方法依赖手工特征和临床专家经验，而机器学习方法虽提高可重复性，但常难以在噪声和异质临床数据中泛化。本研究提出Residual GRU with Multi-Head Self-Attention，一种为表格临床记录设计的紧凑深度学习架构。该模型整合残差双向门控循环单元用于特征列的序列建模、通道重加权块，以及带可学习分类标记的多头自注意力池化以捕获全局上下文。我们在UCI心脏病数据集上使用5折分层交叉验证评估模型，并与逻辑回归、随机森林、支持向量机等经典方法，以及DeepMLP、卷积网络、循环网络和Transformer等现代深度学习基线进行比较。所提模型达到0.861准确率、0.860宏F1、0.908 ROC-AUC和0.904 PR-AUC，优于所有基线。消融研究确认了残差循环、通道门控和注意力池化的各自贡献。t-SNE可视化进一步表明，与原始特征相比，学习到的嵌入在疾病和非疾病类别间展现出更清晰的分离。这些结果表明，轻量混合循环和基于注意力的架构为临床风险预测提供了准确性与效率之间的强平衡，支持在资源受限的医疗环境中部署。

## 🔬 方法详解

论文提出Residual GRU+MHSA模型，整体框架为紧凑深度学习架构，专为表格临床记录设计。关键技术创新点包括：整合残差双向门控循环单元（GRU）对特征列进行序列建模，引入通道重加权块优化特征表示，以及使用带可学习分类标记的多头自注意力（MHSA）池化机制捕获全局依赖关系。与现有方法的主要区别在于，它结合了循环网络的时间建模能力和注意力机制的全局上下文捕捉，形成轻量混合结构，相比传统机器学习方法（如逻辑回归）和单一深度学习模型（如纯Transformer或卷积网络），在保持高效率的同时提升了处理异质临床数据的能力。

## 📊 实验亮点

在UCI心脏病数据集上，模型达到0.861准确率、0.860宏F1、0.908 ROC-AUC和0.904 PR-AUC，全面优于逻辑回归、随机森林、支持向量机及DeepMLP、卷积网络等深度学习基线。消融研究证实残差循环、通道门控和注意力池化均贡献显著性能提升。

## 🎯 应用场景

该研究主要应用于心血管疾病早期检测和风险预测，基于表格临床记录（如患者病史、检查指标）进行分析。潜在价值在于支持资源受限的医疗环境部署，如社区医院或远程医疗，提供高效、自动化的诊断辅助工具，促进早期干预和个性化治疗。

## 📄 摘要（原文）

> Cardiovascular disease (CVD) remains the leading cause of mortality worldwide, underscoring the need for reliable and efficient predictive tools that support early intervention. Traditional diagnostic approaches rely on handcrafted features and clinician expertise, while machine learning methods improve reproducibility but often struggle to generalize across noisy and heterogeneous clinical data. In this work, we propose Residual GRU with Multi-Head Self-Attention, a compact deep learning architecture designed for tabular clinical records. The model integrates residual bidirectional gated recurrent units for sequential modeling of feature columns, a channel reweighting block, and multi-head self-attention pooling with a learnable classification token to capture global context. We evaluate the model on the UCI Heart Disease dataset using 5-fold stratified cross-validation and compare it against classical methods such as Logistic Regression, Random Forest, and Support Vector Machines, as well as modern deep learning baselines including DeepMLP, convolutional networks, recurrent networks, and Transformers. The proposed model achieves an accuracy of 0.861, macro-F1 of 0.860, ROC-AUC of 0.908, and PR-AUC of 0.904, outperforming all baselines. Ablation studies confirm the individual contributions of residual recurrence, channel gating, and attention pooling. t-SNE visualizations further indicate that the learned embeddings exhibit clearer separation between disease and non-disease classes compared to raw features. These results demonstrate that lightweight hybrid recurrent and attention-based architectures provide a strong balance between accuracy and efficiency for clinical risk prediction, supporting deployment in resource-constrained healthcare settings.

