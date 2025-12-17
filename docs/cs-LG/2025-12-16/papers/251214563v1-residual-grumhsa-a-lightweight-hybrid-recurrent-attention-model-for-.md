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

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `心血管疾病检测` `轻量混合架构` `残差双向GRU` `多头自注意力` `表格数据建模` `临床风险预测` `资源受限部署` `深度学习优化`

## 📋 核心要点

1. 心血管疾病检测依赖传统手工特征和专家经验，机器学习方法在噪声和异质临床数据上泛化困难。
2. 提出轻量混合架构，结合残差双向GRU、通道重加权和多头自注意力池化，以捕获序列和全局特征。
3. 在UCI心脏病数据集上，模型准确率达0.861，优于经典和深度学习基线，消融研究验证各模块贡献。

## 📝 摘要（中文）

心血管疾病是全球主要死因，需要可靠高效的预测工具以支持早期干预。传统诊断方法依赖手工特征和临床专家经验，而机器学习方法虽提高可重复性，但常难以在噪声和异质临床数据上泛化。本文提出Residual GRU with Multi-Head Self-Attention，一种为表格临床记录设计的紧凑深度学习架构。该模型集成残差双向门控循环单元用于特征列的序列建模、通道重加权块，以及带可学习分类令牌的多头自注意力池化以捕获全局上下文。我们在UCI心脏病数据集上使用5折分层交叉验证评估模型，并与逻辑回归、随机森林、支持向量机等经典方法，以及DeepMLP、卷积网络、循环网络和Transformer等现代深度学习基线进行比较。所提模型达到0.861的准确率、0.860的宏F1、0.908的ROC-AUC和0.904的PR-AUC，优于所有基线。消融研究确认了残差循环、通道门控和注意力池化的个体贡献。t-SNE可视化进一步表明，与原始特征相比，学习到的嵌入在疾病和非疾病类别间展现出更清晰的分离。这些结果表明，轻量混合循环和基于注意力的架构为临床风险预测提供了准确性与效率之间的强平衡，支持在资源受限的医疗环境中部署。

## 🔬 方法详解

**问题定义**：论文旨在解决心血管疾病检测中，传统方法依赖手工特征和专家经验，而机器学习方法在噪声和异质临床表格数据上泛化能力不足的问题。现有方法的痛点包括特征工程复杂、模型对数据噪声敏感，以及深度学习模型如Transformer计算开销大，不适合资源受限的医疗环境。

**核心思路**：设计一个轻量混合深度学习架构，结合循环神经网络（RNN）的序列建模能力和自注意力机制的全局上下文捕获能力，通过残差连接和通道重加权增强特征表示，以提高模型在临床表格数据上的准确性和泛化性，同时保持计算效率。

**技术框架**：整体架构包括三个主要模块：首先，使用残差双向门控循环单元（Residual Bidirectional GRU）对特征列进行序列建模，处理表格数据的时序或顺序依赖；其次，引入通道重加权块（Channel Reweighting Block），通过注意力机制动态调整特征通道的重要性；最后，采用多头自注意力池化（Multi-Head Self-Attention Pooling）与可学习分类令牌，聚合全局信息并输出分类结果。流程为输入表格数据→残差双向GRU处理→通道重加权→多头自注意力池化→分类输出。

**关键创新**：最重要的技术创新点是轻量混合架构的设计，将残差循环、通道门控和注意力池化有机结合，本质区别在于它避免了传统Transformer的高计算成本，同时通过循环网络捕获局部序列模式，通过注意力机制增强全局特征交互，实现了准确性与效率的平衡。与现有方法相比，它专门针对表格临床数据优化，减少了参数数量，更适合部署在资源受限的医疗场景。

**关键设计**：关键参数设置包括使用双向GRU处理特征序列，隐藏层大小未知；通道重加权块可能基于注意力权重调整特征；多头自注意力池化中，头数未知，但包含可学习分类令牌以聚合信息。损失函数可能使用交叉熵损失进行二分类任务。网络结构紧凑，整体参数较少，以支持轻量化部署。具体超参数如学习率、批次大小在论文中未详细说明，但通过5折分层交叉验证进行优化。

## 📊 实验亮点

在UCI心脏病数据集上，Residual GRU+MHSA模型达到0.861准确率、0.860宏F1、0.908 ROC-AUC和0.904 PR-AUC，优于逻辑回归、随机森林、支持向量机及DeepMLP、卷积网络、循环网络和Transformer等基线。消融研究确认残差循环、通道门控和注意力池化均贡献性能提升，t-SNE可视化显示学习嵌入在类别间分离更清晰，验证了模型的有效性。

## 🎯 应用场景

该研究主要应用于心血管疾病早期检测和风险预测，基于表格临床记录如电子健康档案。其实际价值在于提供高效、准确的自动化诊断工具，支持临床决策，减少对专家经验的依赖。未来影响可能扩展到其他慢性病预测，促进资源受限医疗环境中的智能医疗部署，提升公共卫生水平。

## 📄 摘要（原文）

> Cardiovascular disease (CVD) remains the leading cause of mortality worldwide, underscoring the need for reliable and efficient predictive tools that support early intervention. Traditional diagnostic approaches rely on handcrafted features and clinician expertise, while machine learning methods improve reproducibility but often struggle to generalize across noisy and heterogeneous clinical data. In this work, we propose Residual GRU with Multi-Head Self-Attention, a compact deep learning architecture designed for tabular clinical records. The model integrates residual bidirectional gated recurrent units for sequential modeling of feature columns, a channel reweighting block, and multi-head self-attention pooling with a learnable classification token to capture global context. We evaluate the model on the UCI Heart Disease dataset using 5-fold stratified cross-validation and compare it against classical methods such as Logistic Regression, Random Forest, and Support Vector Machines, as well as modern deep learning baselines including DeepMLP, convolutional networks, recurrent networks, and Transformers. The proposed model achieves an accuracy of 0.861, macro-F1 of 0.860, ROC-AUC of 0.908, and PR-AUC of 0.904, outperforming all baselines. Ablation studies confirm the individual contributions of residual recurrence, channel gating, and attention pooling. t-SNE visualizations further indicate that the learned embeddings exhibit clearer separation between disease and non-disease classes compared to raw features. These results demonstrate that lightweight hybrid recurrent and attention-based architectures provide a strong balance between accuracy and efficiency for clinical risk prediction, supporting deployment in resource-constrained healthcare settings.

