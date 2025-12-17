---
layout: default
title: DriverGaze360: OmniDirectional Driver Attention with Object-Level Guidance
---

# DriverGaze360: OmniDirectional Driver Attention with Object-Level Guidance

**arXiv**: [2512.14266v1](https://arxiv.org/abs/2512.14266) | [PDF](https://arxiv.org/pdf/2512.14266.pdf)

**作者**: Shreedhar Govil, Didier Stricker, Jason Rambach

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出DriverGaze360全景数据集与DriverGaze360-Net模型，以解决自动驾驶中驾驶员注意力预测的视野局限问题。**

🎯 **匹配领域**: **自动驾驶** **视觉里程计**

**关键词**: `驾驶员注意力预测` `全景视觉` `自动驾驶` `语义分割` `数据集构建` `深度学习` `人机交互` `可解释AI`

## 📋 核心要点

1. 现有驾驶员注意力预测方法受限于狭窄前方视野和有限驾驶多样性，无法捕捉变道、转弯等场景的完整空间上下文。
2. 提出DriverGaze360全景数据集和DriverGaze360-Net模型，通过联合学习注意力图和语义分割实现全方位注意力预测。
3. 实验显示DriverGaze360-Net在全景驾驶图像上实现先进性能，显著提升空间感知和预测准确性。

## 📝 摘要（中文）

预测驾驶员注意力是开发可解释自动驾驶系统及理解人机混合交通场景中驾驶员行为的关键问题。尽管通过大规模驾驶员注意力数据集和深度学习架构已取得显著进展，但现有工作受限于狭窄的前方视野和有限的驾驶多样性，无法捕捉驾驶环境的完整空间上下文，特别是在变道、转弯及涉及行人或骑行者等外围物体交互时。本文介绍了DriverGaze360，一个大规模360度视野驾驶员注意力数据集，包含从19名人类驾驶员收集的约100万帧带注视标签的图像，实现了对驾驶员注视行为的全方位建模。此外，我们的全景注意力预测方法DriverGaze360-Net通过采用辅助语义分割头联合学习注意力图和关注对象，提高了对宽全景输入的空间感知和注意力预测能力。大量实验表明，DriverGaze360-Net在全景驾驶图像上实现了多个指标的先进注意力预测性能。数据集和方法可在https://av.dfki.de/drivergaze360获取。

## 🔬 方法详解

DriverGaze360-Net是一个全景注意力预测框架，核心架构包括一个主干网络处理360度输入图像，以及两个并行输出头：一个用于生成注意力图，另一个作为辅助语义分割头识别关注对象。关键技术创新在于联合学习注意力图和语义分割，通过对象级引导增强空间感知能力。与现有方法的主要区别在于其全景视野处理能力和对象级语义融合，突破了传统方法在视野范围和上下文理解上的局限。

## 📊 实验亮点

DriverGaze360-Net在全景驾驶图像上实现先进注意力预测性能，在多个评估指标上超越现有方法，显著提升对变道、转弯等复杂场景的预测准确性。

## 🎯 应用场景

该研究可应用于自动驾驶系统的可解释性开发，帮助理解驾驶员行为，提升人机混合交通场景的安全性，并支持高级驾驶辅助系统（ADAS）的优化设计。

## 📄 摘要（原文）

> Predicting driver attention is a critical problem for developing explainable autonomous driving systems and understanding driver behavior in mixed human-autonomous vehicle traffic scenarios. Although significant progress has been made through large-scale driver attention datasets and deep learning architectures, existing works are constrained by narrow frontal field-of-view and limited driving diversity. Consequently, they fail to capture the full spatial context of driving environments, especially during lane changes, turns, and interactions involving peripheral objects such as pedestrians or cyclists. In this paper, we introduce DriverGaze360, a large-scale 360$^\circ$ field of view driver attention dataset, containing $\sim$1 million gaze-labeled frames collected from 19 human drivers, enabling comprehensive omnidirectional modeling of driver gaze behavior. Moreover, our panoramic attention prediction approach, DriverGaze360-Net, jointly learns attention maps and attended objects by employing an auxiliary semantic segmentation head. This improves spatial awareness and attention prediction across wide panoramic inputs. Extensive experiments demonstrate that DriverGaze360-Net achieves state-of-the-art attention prediction performance on multiple metrics on panoramic driving images. Dataset and method available at https://av.dfki.de/drivergaze360.

