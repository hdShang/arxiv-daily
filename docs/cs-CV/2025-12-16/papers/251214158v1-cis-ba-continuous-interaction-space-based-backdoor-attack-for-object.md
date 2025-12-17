---
layout: default
title: CIS-BA: Continuous Interaction Space Based Backdoor Attack for Object Detection in the Real-World
---

# CIS-BA: Continuous Interaction Space Based Backdoor Attack for Object Detection in the Real-World

**arXiv**: [2512.14158v1](https://arxiv.org/abs/2512.14158) | [PDF](https://arxiv.org/pdf/2512.14158.pdf)

**作者**: Shuxin Zhao, Bo Lang, Nan Xiao, Yilang Zhang

**分类**: cs.CV, cs.CR

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于连续交互空间的后门攻击CIS-BA，以解决真实世界目标检测中现有攻击方法能力与鲁棒性不足的问题。**

**关键词**: `后门攻击` `目标检测` `连续交互空间` `多触发攻击` `鲁棒性攻击` `自动驾驶安全` `样本投毒` `几何约束`

## 📋 核心要点

1. 现有后门攻击依赖单触发-单对象映射和像素级线索，导致能力有限且鲁棒性不足，难以应对真实世界复杂交互场景。
2. CIS-BA将触发设计从静态对象特征转向连续对象间交互模式，通过建模交互空间实现多触发-多对象攻击，提升鲁棒性。
3. 实验显示CIS-BA在复杂环境下攻击成功率超97%，动态多触发条件下有效性超95%，并能规避多种先进防御方法。

## 📝 摘要（中文）

在自动驾驶等真实世界应用中部署的目标检测模型面临后门攻击的严重威胁。尽管现有方法具有实际效果，但由于依赖单触发-单对象映射和脆弱的像素级线索，其能力和鲁棒性存在固有局限。我们提出CIS-BA，一种新颖的后门攻击范式，通过从静态对象特征转向描述场景中对象如何共现和交互的连续对象间交互模式，重新定义触发设计。通过将这些模式建模为连续交互空间，CIS-BA引入了空间触发器，首次实现了多触发-多对象攻击机制，并通过不变的几何关系实现鲁棒性。为实现此范式，我们设计了CIS-Frame，通过交互分析构建空间触发器，将其形式化为类别-几何约束以进行样本投毒，并在检测器训练期间嵌入后门。CIS-Frame支持单对象攻击（对象误分类和消失）和多对象同时攻击，能够在不同交互状态下实现复杂协调的效果。在MS-COCO和真实世界视频上的实验表明，CIS-BA在复杂环境下攻击成功率超过97%，在动态多触发条件下保持超过95%的有效性，同时规避了三种最先进的防御方法。总之，CIS-BA扩展了交互密集场景中的后门攻击格局，并为目标检测系统的安全性提供了新见解。

## 🔬 方法详解

CIS-BA的核心方法基于CIS-Frame框架，整体流程包括：首先通过交互分析构建连续交互空间，将对象间的共现和交互模式建模为空间触发器；其次，将这些触发器形式化为类别-几何约束，用于样本投毒，确保攻击在几何关系上具有不变性；最后，在目标检测器训练过程中嵌入后门，实现攻击的隐蔽性和持久性。关键技术创新点在于首次引入空间触发器概念，从交互模式而非像素层面设计攻击，支持多触发-多对象机制。与现有方法的主要区别在于摆脱了单触发-单对象的局限，利用交互空间的连续性和几何鲁棒性，增强了攻击的复杂性和适应性。

## 📊 实验亮点

CIS-BA在MS-COCO和真实世界视频实验中，攻击成功率超过97%，在动态多触发条件下保持超过95%有效性，成功规避三种最先进防御方法，显著提升了后门攻击的能力和鲁棒性。

## 🎯 应用场景

该研究主要应用于自动驾驶、视频监控等真实世界目标检测系统，揭示后门攻击在交互密集场景中的潜在威胁，为系统安全评估和防御设计提供新视角，具有重要的实际安全价值。

## 📄 摘要（原文）

> Object detection models deployed in real-world applications such as autonomous driving face serious threats from backdoor attacks. Despite their practical effectiveness,existing methods are inherently limited in both capability and robustness due to their dependence on single-trigger-single-object mappings and fragile pixel-level cues. We propose CIS-BA, a novel backdoor attack paradigm that redefines trigger design by shifting from static object features to continuous inter-object interaction patterns that describe how objects co-occur and interact in a scene. By modeling these patterns as a continuous interaction space, CIS-BA introduces space triggers that, for the first time, enable a multi-trigger-multi-object attack mechanism while achieving robustness through invariant geometric relations. To implement this paradigm, we design CIS-Frame, which constructs space triggers via interaction analysis, formalizes them as class-geometry constraints for sample poisoning, and embeds the backdoor during detector training. CIS-Frame supports both single-object attacks (object misclassification and disappearance) and multi-object simultaneous attacks, enabling complex and coordinated effects across diverse interaction states. Experiments on MS-COCO and real-world videos show that CIS-BA achieves over 97% attack success under complex environments and maintains over 95% effectiveness under dynamic multi-trigger conditions, while evading three state-of-the-art defenses. In summary, CIS-BA extends the landscape of backdoor attacks in interaction-intensive scenarios and provides new insights into the security of object detection systems.

