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

**提出Residual GRU+MHSA轻量级混合循环注意力模型，用于心血管疾病检测。**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)**

**关键词**: `心血管疾病检测` `循环神经网络` `自注意力机制` `深度学习` `临床数据分析`

## 📋 核心要点

1. 现有心血管疾病诊断方法依赖手工特征，机器学习方法泛化性差，难以处理临床数据的噪声和异构性。
2. 提出Residual GRU+MHSA模型，利用残差GRU进行序列建模，通道重加权和多头自注意力捕获全局上下文。
3. 实验结果表明，该模型在UCI心脏病数据集上优于传统机器学习和深度学习基线，具有更高的准确率和效率。

## 📝 摘要（中文）

心血管疾病(CVD)仍然是全球主要的死亡原因，因此需要可靠和高效的预测工具来支持早期干预。传统诊断方法依赖于手工特征和临床医生专业知识，而机器学习方法提高了可重复性，但通常难以推广到嘈杂和异构的临床数据。本文提出了一种紧凑的深度学习架构：带有Multi-Head Self-Attention的Residual GRU，专为表格临床记录设计。该模型集成了残差双向门控循环单元，用于特征列的序列建模，一个通道重加权块，以及带有可学习分类token的多头自注意力池化，以捕获全局上下文。在UCI心脏病数据集上，使用5折分层交叉验证评估了该模型，并将其与经典方法（如Logistic Regression、Random Forest和Support Vector Machines）以及现代深度学习基线（包括DeepMLP、卷积网络、循环网络和Transformers）进行了比较。所提出的模型实现了0.861的准确率、0.860的macro-F1、0.908的ROC-AUC和0.904的PR-AUC，优于所有基线。消融研究证实了残差循环、通道门控和注意力池化的各自贡献。t-SNE可视化进一步表明，与原始特征相比，学习到的嵌入在疾病和非疾病类别之间表现出更清晰的分离。这些结果表明，轻量级混合循环和基于注意力的架构在临床风险预测的准确性和效率之间提供了强大的平衡，支持在资源受限的医疗环境中部署。

## 🔬 方法详解

**问题定义**：论文旨在解决心血管疾病（CVD）的早期预测问题。现有方法，如传统机器学习和深度学习模型，在处理临床表格数据时存在局限性。传统方法依赖手工特征工程，耗时且依赖专家知识。深度学习模型虽然可以自动学习特征，但往往难以在噪声较大、异构性强的临床数据上泛化，并且计算复杂度较高，不利于在资源受限的环境中部署。

**核心思路**：论文的核心思路是结合循环神经网络（RNN）和自注意力机制的优势，设计一个轻量级的混合模型。循环神经网络擅长处理序列数据，可以捕捉特征之间的时序关系。自注意力机制可以捕捉全局上下文信息，并对重要特征进行加权。通过残差连接、通道重加权等技术，进一步提升模型的性能和鲁棒性。

**技术框架**：该模型主要包含以下几个模块：1) **Residual Bidirectional GRU**：使用双向GRU对特征列进行序列建模，并采用残差连接加速收敛。2) **Channel Reweighting Block**：对不同特征通道进行重加权，突出重要特征。3) **Multi-Head Self-Attention Pooling**：使用多头自注意力机制对GRU的输出进行池化，并引入一个可学习的分类token，用于捕获全局上下文信息。4) **分类器**：使用全连接层进行最终的分类。

**关键创新**：该论文的关键创新在于将残差GRU、通道重加权和多头自注意力池化相结合，构建了一个轻量级的混合模型。这种混合架构既能捕捉特征之间的时序关系，又能捕捉全局上下文信息，同时保持较低的计算复杂度。此外，使用可学习的分类token，使得模型能够更好地学习全局表示。

**关键设计**：模型使用双向GRU，可以同时考虑特征的前向和后向关系。残差连接可以缓解梯度消失问题，加速模型收敛。通道重加权模块使用SE (Squeeze-and-Excitation) block，自适应地学习不同通道的重要性。多头自注意力机制使用8个head。损失函数使用二元交叉熵损失函数。模型使用Adam优化器进行训练，学习率为0.001，batch size为32。

## 📊 实验亮点

该模型在UCI心脏病数据集上取得了显著的性能提升，准确率达到0.861，macro-F1达到0.860，ROC-AUC达到0.908，PR-AUC达到0.904，优于Logistic Regression、Random Forest、SVM、DeepMLP、CNN、RNN和Transformer等基线模型。消融实验表明，残差连接、通道重加权和多头自注意力机制都对性能提升有贡献。

## 🎯 应用场景

该研究成果可应用于心血管疾病的早期风险预测，辅助医生进行诊断和制定治疗方案。该模型具有轻量级的特点，易于部署在资源受限的医疗环境中，例如基层医院和移动医疗设备。未来，该模型可以扩展到其他疾病的预测，并与其他临床数据（如影像数据、基因数据）相结合，提高预测的准确性和可靠性。

## 📄 摘要（原文）

> Cardiovascular disease (CVD) remains the leading cause of mortality worldwide, underscoring the need for reliable and efficient predictive tools that support early intervention. Traditional diagnostic approaches rely on handcrafted features and clinician expertise, while machine learning methods improve reproducibility but often struggle to generalize across noisy and heterogeneous clinical data. In this work, we propose Residual GRU with Multi-Head Self-Attention, a compact deep learning architecture designed for tabular clinical records. The model integrates residual bidirectional gated recurrent units for sequential modeling of feature columns, a channel reweighting block, and multi-head self-attention pooling with a learnable classification token to capture global context. We evaluate the model on the UCI Heart Disease dataset using 5-fold stratified cross-validation and compare it against classical methods such as Logistic Regression, Random Forest, and Support Vector Machines, as well as modern deep learning baselines including DeepMLP, convolutional networks, recurrent networks, and Transformers. The proposed model achieves an accuracy of 0.861, macro-F1 of 0.860, ROC-AUC of 0.908, and PR-AUC of 0.904, outperforming all baselines. Ablation studies confirm the individual contributions of residual recurrence, channel gating, and attention pooling. t-SNE visualizations further indicate that the learned embeddings exhibit clearer separation between disease and non-disease classes compared to raw features. These results demonstrate that lightweight hybrid recurrent and attention-based architectures provide a strong balance between accuracy and efficiency for clinical risk prediction, supporting deployment in resource-constrained healthcare settings.

