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

**提出Residual GRU+MHSA轻量混合循环注意力模型，以提升心血管疾病检测的准确性和效率。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `心血管疾病检测` `轻量深度学习` `残差循环网络` `多头自注意力` `临床风险预测` `表格数据处理` `医疗人工智能` `模型效率优化`

## 📋 核心要点

1. 现有方法依赖手工特征或难以泛化到噪声临床数据，限制了心血管疾病预测的可靠性。
2. 提出Residual GRU+MHSA模型，结合残差循环单元和注意力机制，以轻量架构捕获序列和全局特征。
3. 在UCI数据集上，模型准确率达0.861，优于传统和深度学习基线，并通过消融验证了组件有效性。

## 📝 摘要（中文）

心血管疾病是全球主要死因，需要可靠高效的预测工具以支持早期干预。传统诊断方法依赖手工特征和临床专家经验，而机器学习方法虽提高可重复性，但常难以泛化到噪声和异构临床数据。本研究提出Residual GRU with Multi-Head Self-Attention，一种紧凑的深度学习架构，专为表格临床记录设计。该模型集成残差双向门控循环单元用于特征列的序列建模、通道重加权块，以及带可学习分类令牌的多头自注意力池化以捕获全局上下文。我们在UCI心脏病数据集上使用5折分层交叉验证评估模型，并与逻辑回归、随机森林、支持向量机等经典方法，以及DeepMLP、卷积网络、循环网络和Transformer等现代深度学习基线进行比较。所提模型达到0.861的准确率、0.860的宏F1、0.908的ROC-AUC和0.904的PR-AUC，优于所有基线。消融研究确认了残差循环、通道门控和注意力池化的个体贡献。t-SNE可视化进一步表明，与原始特征相比，学习到的嵌入在疾病和非疾病类别间展现出更清晰的分离。这些结果表明，轻量混合循环和注意力架构在临床风险预测中提供了准确性和效率之间的强平衡，支持在资源受限的医疗环境中部署。

## 🔬 方法详解

整体框架为轻量混合模型，专为表格临床数据设计。关键技术创新包括：使用残差双向GRU处理特征列序列，增强梯度流动；引入通道重加权块动态调整特征重要性；结合多头自注意力池化与可学习分类令牌，捕获全局上下文并优化分类。与现有方法的主要区别在于，它融合循环和注意力机制于紧凑架构，避免了传统方法的手工特征依赖和深度学习模型的过参数化，实现高效且准确的预测。

## 📊 实验亮点

模型在UCI心脏病数据集上取得0.861准确率、0.860宏F1、0.908 ROC-AUC和0.904 PR-AUC，全面超越逻辑回归、随机森林、支持向量机及DeepMLP、卷积网络、循环网络和Transformer等基线，并通过消融和t-SNE可视化验证了组件贡献和特征分离效果。

## 🎯 应用场景

该研究可应用于心血管疾病早期筛查和风险预测，特别适合资源受限的医疗环境，如社区诊所或远程医疗系统，通过轻量模型部署提升诊断效率和可及性。

## 📄 摘要（原文）

> Cardiovascular disease (CVD) remains the leading cause of mortality worldwide, underscoring the need for reliable and efficient predictive tools that support early intervention. Traditional diagnostic approaches rely on handcrafted features and clinician expertise, while machine learning methods improve reproducibility but often struggle to generalize across noisy and heterogeneous clinical data. In this work, we propose Residual GRU with Multi-Head Self-Attention, a compact deep learning architecture designed for tabular clinical records. The model integrates residual bidirectional gated recurrent units for sequential modeling of feature columns, a channel reweighting block, and multi-head self-attention pooling with a learnable classification token to capture global context. We evaluate the model on the UCI Heart Disease dataset using 5-fold stratified cross-validation and compare it against classical methods such as Logistic Regression, Random Forest, and Support Vector Machines, as well as modern deep learning baselines including DeepMLP, convolutional networks, recurrent networks, and Transformers. The proposed model achieves an accuracy of 0.861, macro-F1 of 0.860, ROC-AUC of 0.908, and PR-AUC of 0.904, outperforming all baselines. Ablation studies confirm the individual contributions of residual recurrence, channel gating, and attention pooling. t-SNE visualizations further indicate that the learned embeddings exhibit clearer separation between disease and non-disease classes compared to raw features. These results demonstrate that lightweight hybrid recurrent and attention-based architectures provide a strong balance between accuracy and efficiency for clinical risk prediction, supporting deployment in resource-constrained healthcare settings.

