---
layout: default
title: Towards Cross-View Point Correspondence in Vision-Language Models
---

# Towards Cross-View Point Correspondence in Vision-Language Models

**arXiv**: [2512.04686v2](https://arxiv.org/abs/2512.04686) | [PDF](https://arxiv.org/pdf/2512.04686.pdf)

**作者**: Yipu Wang, Yuheng Ji, Yuyang Liu, Enshen Zhou, Ziqiang Yang, Yuxuan Tian, Ziheng Qin, Yue Liu, Huajie Tan, Cheng Chi, Zhiyuan Ma, Daniel Dajun Zeng, Xiaolong Zheng

**分类**: cs.CV

**发布日期**: 2025-12-04 (更新: 2025-12-07)

**🔗 代码/项目**: [GITHUB](https://github.com/WangYipu2002/CrossPoint)

---

## 💡 一句话要点

**提出CrossPoint-Bench和CroPond模型，解决视觉语言模型中跨视角点对应难题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `跨视角对应` `视觉语言模型` `点对应` `基准测试` `数据集` `具身智能` `机器人导航`

## 📋 核心要点

1. 现有视觉语言模型在跨视角点对应方面存在不足，尤其是在精确点级对应上，限制了其在具身智能中的应用。
2. 提出CrossPoint-Bench基准测试和CrossPoint-378K数据集，并设计CroPond模型，以提升模型在跨视角点对应任务上的性能。
3. 实验结果表明，CroPond模型在CrossPoint-Bench上超越了Gemini-2.5-Pro，准确率提升了39.7%，显著提高了跨视角点对应的精度。

## 📝 摘要（中文）

跨视角对应是空间理解和具身智能的一项基本能力。然而，视觉语言模型(VLMs)在这方面仍有不足，尤其是在实现精确的点级对应方面，这对于精确的交互至关重要。因此，我们提出了跨视角点对应(CVPC)任务和CrossPoint-Bench，这是一个综合性的基准，其分层设计灵感来源于人类“感知”、“推理”和“对应”的认知过程。我们的评估表明，最先进的模型(例如，Gemini-2.5-Pro)仍然远远落后于人类，总体准确率差距超过54.65%，这暴露了从粗粒度判断到细粒度坐标预测的挑战。为了解决这个问题，我们构建了CrossPoint-378K数据集，其中包含900个场景中378K个问答对，重点关注可操作的区域，更好地反映了现实世界的操作和交互场景。此外，我们提出了在CrossPoint-378K数据集上训练的CroPond。我们的CroPond在CrossPoint-Bench上实现了最先进的性能，准确率超过Gemini-2.5-Pro 39.7%，这为推进未来跨视角对应工作奠定了基础。该基准、数据集和模型已在https://github.com/WangYipu2002/CrossPoint公开发布。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉语言模型在跨视角场景下，难以建立精确点对应关系的问题。现有方法通常只能进行粗粒度的判断，无法准确预测目标点在不同视角下的坐标，这限制了其在需要精细操作的具身智能任务中的应用。

**核心思路**：论文的核心思路是构建一个更具挑战性的基准测试CrossPoint-Bench和一个大规模数据集CrossPoint-378K，并在此基础上训练一个专门的模型CroPond。通过更细粒度的数据和更有效的训练方法，提升模型在跨视角点对应任务上的性能。

**技术框架**：整体框架包含三个主要部分：1) CrossPoint-Bench基准测试，用于评估模型在跨视角点对应任务上的性能；2) CrossPoint-378K数据集，包含大量不同视角下的问答对，用于训练模型；3) CroPond模型，基于视觉语言模型架构，通过在CrossPoint-378K数据集上进行训练，提升跨视角点对应的能力。

**关键创新**：论文的关键创新在于：1) 提出了CrossPoint-Bench基准测试，该基准测试更具挑战性，能够更全面地评估模型在跨视角点对应任务上的性能；2) 构建了CrossPoint-378K数据集，该数据集包含大量高质量的问答对，能够有效提升模型的训练效果；3) 提出了CroPond模型，该模型在CrossPoint-Bench上取得了显著的性能提升。

**关键设计**：CrossPoint-Bench基准测试采用分层设计，模拟人类的认知过程，包含“感知”、“推理”和“对应”三个阶段。CrossPoint-378K数据集重点关注可操作的区域，更好地反映了现实世界的操作和交互场景。CroPond模型的具体网络结构和损失函数等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

CroPond模型在CrossPoint-Bench基准测试上取得了显著的性能提升，准确率超过了Gemini-2.5-Pro 39.7%。这一结果表明，通过构建更具挑战性的基准测试和更大规模的数据集，并在此基础上进行针对性的模型训练，可以有效提升视觉语言模型在跨视角点对应任务上的性能。

## 🎯 应用场景

该研究成果可应用于机器人导航、物体抓取、增强现实等领域。通过提升视觉语言模型在跨视角点对应方面的能力，可以使机器人更好地理解周围环境，并进行更精确的操作。例如，机器人可以根据用户的指令，在不同视角下准确找到目标物体并进行抓取，从而实现更智能的人机交互。

## 📄 摘要（原文）

> Cross-view correspondence is a fundamental capability for spatial understanding and embodied AI. However, it is still far from being realized in Vision-Language Models (VLMs), especially in achieving precise point-level correspondence, which is crucial for precise affordance interaction. So we propose the Cross-View Point Correspondence (CVPC) task and CrossPoint-Bench, a comprehensive benchmark with hierarchical design, inspired by the human cognitive process of "perceive", "reason", and "correspond". Our evaluation shows the state-of-the-art models (e.g., Gemini-2.5-Pro) still fall far behind humans, with a gap of over 54.65% in overall accuracy, exposing a challenge in transitioning from coarse-grained judgement to fine-grained coordinate prediction. To address this problem, we construct CrossPoint-378K, a dataset with 378K question-answering pairs across 900 scenes, focused on actionable affordance regions that better reflect real-world manipulation and interaction scenarios. Furthermore, we propose CroPond that trained on the CrossPoint-378K dataset. Our CroPond achieves state-of-the-art performance on CrossPoint-Bench, surpassing Gemini-2.5-Pro by 39.7% accuracy, which offers a foundation for advancing future work on cross-view correspondence. The benchmark, dataset, and model are publicly available at https://github.com/WangYipu2002/CrossPoint.

