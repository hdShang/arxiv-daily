---
layout: default
title: CAPRMIL: Context-Aware Patch Representations for Multiple Instance Learning
---

# CAPRMIL: Context-Aware Patch Representations for Multiple Instance Learning

**arXiv**: [2512.14540v1](https://arxiv.org/abs/2512.14540) | [PDF](https://arxiv.org/pdf/2512.14540.pdf)

**作者**: Andreas Lolos, Theofilos Christodoulou, Aris L. Moustakas, Stergios Christodoulidis, Maria Vakalopoulou

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: 24 pages, 12 Figures, 4 Tables

**🔗 代码/项目**: [GITHUB](https://github.com/mandlos/CAPRMIL)

---

## 💡 一句话要点

**提出CAPRMIL框架，通过上下文感知的补丁表示简化多示例学习，提升计算病理学中的弱监督分析效率。**

**关键词**: `多示例学习` `计算病理学` `弱监督学习` `上下文感知表示` `全切片图像分析` `高效聚合` `线性复杂度` `医疗图像处理`

## 📋 核心要点

1. 现有MIL方法依赖复杂注意力聚合，计算开销大，难以高效处理大规模WSI数据。
2. 提出CAPRMIL框架，通过上下文感知补丁嵌入和线性复杂度全局上下文注入，简化聚合过程。
3. 在多个病理基准测试中匹配SOTA性能，显著降低参数、FLOPs和内存需求，提升训练效率。

## 📝 摘要（中文）

在计算病理学中，由于全切片图像（WSI）的千兆像素尺度和像素级标注的稀缺性，弱监督已成为深度学习的标准方法，其中多示例学习（MIL）被确立为切片级模型训练的主要框架。本文受神经偏微分方程（PDE）求解器的启发，为MIL方法引入了一种新颖的设置。我们提出了一种高效、聚合器无关的框架，无需依赖复杂的基于注意力的聚合，而是从MIL聚合器中移除了相关性学习的复杂性。CAPRMIL生成丰富的上下文感知补丁嵌入，促进下游任务中的有效相关性学习。通过将使用冻结补丁编码器提取的补丁特征投影到一小组全局上下文/形态感知令牌中，并利用多头自注意力，CAPRMIL以相对于包大小的线性计算复杂度注入全局上下文。结合简单的平均MIL聚合器，CAPRMIL在多个公共病理学基准测试中匹配了最先进的切片级性能，同时与最先进的MIL方法相比，可训练参数总数减少了48%-92.8%，推理期间的FLOPs降低了52%-99%，并在GPU内存效率和训练时间方面排名最佳模型之列。我们的结果表明，在聚合之前学习丰富的上下文感知实例表示是复杂池化方法在全切片分析中的一种有效且可扩展的替代方案。我们的代码可在https://github.com/mandlos/CAPRMIL获取。

## 🔬 方法详解

CAPRMIL的整体框架包括：使用冻结的补丁编码器提取补丁特征，然后将其投影到少量全局上下文/形态感知令牌中，通过多头自注意力机制注入全局上下文，计算复杂度与包大小呈线性关系。关键技术创新点在于将相关性学习从聚合器转移到补丁表示阶段，生成上下文感知的嵌入，从而允许使用简单的平均聚合器。与现有方法的主要区别在于，它避免了复杂的注意力聚合机制，通过高效的上下文注入实现高性能，减少了模型复杂性和计算资源需求。

## 📊 实验亮点

CAPRMIL在多个公共病理学基准测试中匹配最先进性能，同时可训练参数减少48%-92.8%，推理FLOPs降低52%-99%，在GPU内存效率和训练时间方面表现优异，显著提升了计算效率。

## 🎯 应用场景

该研究主要应用于计算病理学领域，特别是全切片图像（WSI）的弱监督分析，如癌症诊断、组织分类和预后预测。其高效性使其适合大规模医疗图像处理，降低计算成本，促进临床部署和实时分析。

## 📄 摘要（原文）

> In computational pathology, weak supervision has become the standard for deep learning due to the gigapixel scale of WSIs and the scarcity of pixel-level annotations, with Multiple Instance Learning (MIL) established as the principal framework for slide-level model training. In this paper, we introduce a novel setting for MIL methods, inspired by proceedings in Neural Partial Differential Equation (PDE) Solvers. Instead of relying on complex attention-based aggregation, we propose an efficient, aggregator-agnostic framework that removes the complexity of correlation learning from the MIL aggregator. CAPRMIL produces rich context-aware patch embeddings that promote effective correlation learning on downstream tasks. By projecting patch features -- extracted using a frozen patch encoder -- into a small set of global context/morphology-aware tokens and utilizing multi-head self-attention, CAPRMIL injects global context with linear computational complexity with respect to the bag size. Paired with a simple Mean MIL aggregator, CAPRMIL matches state-of-the-art slide-level performance across multiple public pathology benchmarks, while reducing the total number of trainable parameters by 48%-92.8% versus SOTA MILs, lowering FLOPs during inference by 52%-99%, and ranking among the best models on GPU memory efficiency and training time. Our results indicate that learning rich, context-aware instance representations before aggregation is an effective and scalable alternative to complex pooling for whole-slide analysis. Our code is available at https://github.com/mandlos/CAPRMIL

