---
layout: default
title: ProtoFlow: Interpretable and Robust Surgical Workflow Modeling with Learned Dynamic Scene Graph Prototypes
---

# ProtoFlow: Interpretable and Robust Surgical Workflow Modeling with Learned Dynamic Scene Graph Prototypes

**arXiv**: [2512.14092v1](https://arxiv.org/abs/2512.14092) | [PDF](https://arxiv.org/pdf/2512.14092.pdf)

**作者**: Felix Holm, Ghazal Ghazaei, Nassir Navab

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出ProtoFlow框架，通过动态场景图原型学习实现可解释且鲁棒的手术工作流建模**

**关键词**: `手术工作流建模` `动态场景图` `原型学习` `图神经网络` `可解释人工智能` `少样本学习` `自监督预训练` `医疗图像分析`

## 📋 核心要点

1. 核心问题：手术识别面临高标注成本、数据稀缺和模型缺乏可解释性，现有场景图方法潜力未充分发挥。
2. 方法要点：提出ProtoFlow框架，结合自监督预训练和原型微调，学习动态场景图原型以建模手术工作流。
3. 实验或效果：在CAT-SG数据集上超越GNN基线，少样本场景下鲁棒性强，原型提供可解释的手术洞察。

## 📝 摘要（中文）

目的：详细的手术识别对推进AI辅助手术至关重要，但高标注成本、数据稀缺和缺乏可解释模型阻碍了进展。虽然场景图为手术事件提供了结构化抽象，但其全部潜力尚未被充分挖掘。本研究提出ProtoFlow，一种新颖框架，通过学习动态场景图原型，以可解释且鲁棒的方式建模复杂手术工作流。方法：ProtoFlow采用图神经网络编码器-解码器架构，结合自监督预训练进行丰富表示学习，以及基于原型的微调阶段。该过程发现并精炼核心原型，这些原型封装了重复出现、具有临床意义的手术交互模式，为工作流分析形成可解释的基础。结果：我们在细粒度CAT-SG数据集上评估了该方法。ProtoFlow不仅在整体准确率上优于标准GNN基线，还在有限数据、少样本场景中表现出卓越的鲁棒性，在仅用一个手术视频训练时仍保持强劲性能。定性分析进一步显示，学习到的原型成功识别了不同的手术子技术，并为工作流偏差和罕见并发症提供了清晰、可解释的洞察。结论：通过将鲁棒表示学习与内在可解释性相结合，ProtoFlow代表了向开发更透明、可靠和数据高效AI系统迈出的重要一步，加速了其在手术培训、实时决策支持和工作流优化中的临床应用潜力。

## 🔬 方法详解

ProtoFlow采用图神经网络编码器-解码器架构，整体框架包括自监督预训练和基于原型的微调两个阶段。关键技术创新点在于学习动态场景图原型，这些原型自动发现并封装手术中的重复交互模式，形成可解释的工作流表示。与现有方法的主要区别在于将原型学习引入手术场景图建模，增强了模型的解释性和数据效率，而传统GNN方法通常缺乏这种内在可解释性，且对数据量要求较高。

## 📊 实验亮点

在CAT-SG数据集上，ProtoFlow整体准确率优于标准GNN基线；在少样本场景下表现出卓越鲁棒性，仅用一个手术视频训练时性能仍强劲；定性分析显示学习原型能识别手术子技术并提供工作流偏差的可解释洞察。

## 🎯 应用场景

该研究可应用于手术培训系统，提供可解释的工作流分析辅助教学；在实时手术决策支持中，帮助识别工作流偏差和并发症；还可用于手术室工作流优化，提升手术效率和安全性。

## 📄 摘要（原文）

> Purpose: Detailed surgical recognition is critical for advancing AI-assisted surgery, yet progress is hampered by high annotation costs, data scarcity, and a lack of interpretable models. While scene graphs offer a structured abstraction of surgical events, their full potential remains untapped. In this work, we introduce ProtoFlow, a novel framework that learns dynamic scene graph prototypes to model complex surgical workflows in an interpretable and robust manner.
>   Methods: ProtoFlow leverages a graph neural network (GNN) encoder-decoder architecture that combines self-supervised pretraining for rich representation learning with a prototype-based fine-tuning stage. This process discovers and refines core prototypes that encapsulate recurring, clinically meaningful patterns of surgical interaction, forming an explainable foundation for workflow analysis.
>   Results: We evaluate our approach on the fine-grained CAT-SG dataset. ProtoFlow not only outperforms standard GNN baselines in overall accuracy but also demonstrates exceptional robustness in limited-data, few-shot scenarios, maintaining strong performance when trained on as few as one surgical video. Our qualitative analyses further show that the learned prototypes successfully identify distinct surgical sub-techniques and provide clear, interpretable insights into workflow deviations and rare complications.
>   Conclusion: By uniting robust representation learning with inherent explainability, ProtoFlow represents a significant step toward developing more transparent, reliable, and data-efficient AI systems, accelerating their potential for clinical adoption in surgical training, real-time decision support, and workflow optimization.

