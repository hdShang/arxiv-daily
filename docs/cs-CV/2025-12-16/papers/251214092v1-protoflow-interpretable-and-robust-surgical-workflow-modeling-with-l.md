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

**ProtoFlow：利用动态场景图原型，实现可解释且鲁棒的手术工作流建模**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)** **动作生成与物理动画 (Animation & Physics)** **具身智能与表征学习 (Embodied AI & Representation)**

**关键词**: `手术工作流建模` `动态场景图` `图神经网络` `原型学习` `自监督学习`

## 📋 核心要点

1. 手术识别面临数据稀缺、标注成本高昂以及模型缺乏可解释性的挑战，阻碍了AI辅助手术的发展。
2. ProtoFlow通过学习动态场景图原型来建模手术工作流，利用图神经网络和自监督学习提升模型鲁棒性与可解释性。
3. 实验表明，ProtoFlow在准确性和鲁棒性上优于传统GNN，尤其在少样本情况下表现出色，并能有效识别手术子技术。

## 📝 摘要（中文）

本文提出ProtoFlow，一个新颖的框架，通过学习动态场景图原型来建模复杂的手术工作流，旨在解决手术识别中数据稀缺、标注成本高和缺乏可解释性模型的问题。ProtoFlow利用图神经网络（GNN）编码器-解码器架构，结合自监督预训练以学习丰富的表示，以及基于原型的微调阶段。该过程发现并优化核心原型，这些原型封装了手术交互中重复出现的、具有临床意义的模式，为工作流分析奠定了可解释的基础。在CAT-SG数据集上的评估表明，ProtoFlow不仅在整体准确性上优于标准GNN基线，而且在有限数据和少样本场景中表现出卓越的鲁棒性，即使仅用一个手术视频进行训练也能保持强大的性能。定性分析进一步表明，学习到的原型成功识别了不同的手术子技术，并为工作流偏差和罕见并发症提供了清晰、可解释的见解。ProtoFlow将鲁棒的表示学习与固有的可解释性相结合，代表着朝着开发更透明、可靠和数据高效的AI系统迈出的重要一步，加速了其在手术培训、实时决策支持和工作流优化中的临床应用潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决手术工作流建模中数据稀缺、标注成本高昂以及模型缺乏可解释性的问题。现有方法难以在数据有限的情况下进行有效的学习，并且缺乏对手术过程的清晰解释，限制了其在临床环境中的应用。

**核心思路**：ProtoFlow的核心思路是学习一组具有代表性的“原型”场景图，这些原型能够捕捉手术过程中的关键交互模式。通过将新的手术场景与这些原型进行比较，模型可以识别手术阶段、检测异常情况，并提供对手术过程的解释。这种基于原型的方法提高了模型的鲁棒性和可解释性。

**技术框架**：ProtoFlow采用图神经网络（GNN）编码器-解码器架构。首先，使用自监督学习方法对GNN编码器进行预训练，使其能够学习到丰富的场景图表示。然后，通过原型学习模块，从预训练的表示中提取一组具有代表性的原型。最后，使用解码器将这些原型映射回场景图，并进行手术工作流的分析和预测。整个框架包含预训练、原型学习和微调三个主要阶段。

**关键创新**：ProtoFlow的关键创新在于将原型学习与动态场景图建模相结合。通过学习一组具有代表性的原型，模型能够更好地泛化到新的手术场景，并且提供对手术过程的清晰解释。此外，自监督预训练方法也提高了模型在数据有限情况下的学习能力。

**关键设计**：ProtoFlow使用对比学习作为自监督预训练的目标，鼓励模型学习到区分不同场景图的能力。原型学习模块使用k-means聚类算法从预训练的场景图表示中提取原型。损失函数包括重构损失和对比损失，用于优化原型和解码器。GNN采用Graph Attention Network (GAT)结构，以更好地捕捉节点之间的关系。

## 📊 实验亮点

ProtoFlow在CAT-SG数据集上取得了显著的成果，在整体准确性上优于标准GNN基线。更重要的是，ProtoFlow在有限数据和少样本场景中表现出卓越的鲁棒性，即使仅用一个手术视频进行训练也能保持强大的性能。定性分析表明，学习到的原型能够成功识别不同的手术子技术，并为工作流偏差和罕见并发症提供清晰、可解释的见解。

## 🎯 应用场景

ProtoFlow具有广泛的应用前景，包括手术培训、实时决策支持和工作流优化。它可以帮助医生更好地理解手术过程，提高手术质量和安全性。在手术培训中，ProtoFlow可以用于评估学员的手术技能，并提供个性化的反馈。在实时决策支持中，它可以帮助医生检测手术中的异常情况，并提供相应的建议。在工作流优化中，它可以用于分析手术流程，发现瓶颈并进行改进。

## 📄 摘要（原文）

> Purpose: Detailed surgical recognition is critical for advancing AI-assisted surgery, yet progress is hampered by high annotation costs, data scarcity, and a lack of interpretable models. While scene graphs offer a structured abstraction of surgical events, their full potential remains untapped. In this work, we introduce ProtoFlow, a novel framework that learns dynamic scene graph prototypes to model complex surgical workflows in an interpretable and robust manner.
>   Methods: ProtoFlow leverages a graph neural network (GNN) encoder-decoder architecture that combines self-supervised pretraining for rich representation learning with a prototype-based fine-tuning stage. This process discovers and refines core prototypes that encapsulate recurring, clinically meaningful patterns of surgical interaction, forming an explainable foundation for workflow analysis.
>   Results: We evaluate our approach on the fine-grained CAT-SG dataset. ProtoFlow not only outperforms standard GNN baselines in overall accuracy but also demonstrates exceptional robustness in limited-data, few-shot scenarios, maintaining strong performance when trained on as few as one surgical video. Our qualitative analyses further show that the learned prototypes successfully identify distinct surgical sub-techniques and provide clear, interpretable insights into workflow deviations and rare complications.
>   Conclusion: By uniting robust representation learning with inherent explainability, ProtoFlow represents a significant step toward developing more transparent, reliable, and data-efficient AI systems, accelerating their potential for clinical adoption in surgical training, real-time decision support, and workflow optimization.

