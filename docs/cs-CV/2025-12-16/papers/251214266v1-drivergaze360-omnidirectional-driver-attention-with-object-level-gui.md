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

**提出DriverGaze360数据集和全景注意力预测方法，以解决自动驾驶中驾驶员注意力建模的视野限制问题。**

**关键词**: `驾驶员注意力预测` `全景视野建模` `自动驾驶系统` `语义分割` `深度学习` `混合交通场景` `可解释性` `数据集构建`

## 📋 核心要点

1. 现有方法受限于狭窄前方视野和有限驾驶多样性，无法捕捉变道、转弯等场景的完整空间上下文。
2. 提出DriverGaze360数据集和全景注意力预测方法，联合学习注意力图和关注对象以增强空间感知。
3. 实验显示DriverGaze360-Net在全景驾驶图像上实现了多个指标的先进性能，提升了注意力预测准确性。

## 📝 摘要（中文）

预测驾驶员注意力是开发可解释自动驾驶系统和理解混合交通场景中驾驶员行为的关键问题。尽管通过大规模数据集和深度学习架构已取得显著进展，但现有工作受限于狭窄的前方视野和有限的驾驶多样性，无法捕捉驾驶环境的完整空间上下文，尤其是在变道、转弯和涉及行人或自行车等外围物体交互时。本文介绍了DriverGaze360，一个大规模360度视野驾驶员注意力数据集，包含从19名驾驶员收集的约100万帧注视标记帧，实现了对驾驶员注视行为的全方位建模。此外，我们的全景注意力预测方法DriverGaze360-Net通过采用辅助语义分割头联合学习注意力图和关注对象，提高了对宽全景输入的空间感知和注意力预测能力。大量实验表明，DriverGaze360-Net在全景驾驶图像上实现了多个指标的先进注意力预测性能。数据集和方法可在https://av.dfki.de/drivergaze360获取。

## 🔬 方法详解

论文的核心方法是DriverGaze360-Net，这是一个全景注意力预测模型，整体框架基于深度学习架构，处理360度视野输入以生成注意力图。关键技术创新点在于联合学习注意力图和关注对象，通过引入辅助语义分割头，模型不仅能预测驾驶员注视位置，还能识别被关注的对象类别，如行人或车辆，从而增强空间上下文理解。与现有方法的主要区别在于其全景视野处理能力，克服了传统方法局限于前方视野的不足，并整合了对象级指导，提高了预测的准确性和可解释性。

## 📊 实验亮点

DriverGaze360-Net在全景驾驶图像上实现了多个指标的先进性能，包括注意力预测准确性和空间感知能力，显著优于现有方法，验证了全景视野和对象级指导的有效性。

## 🎯 应用场景

该研究可应用于自动驾驶系统开发，通过预测驾驶员注意力增强车辆的可解释性和安全性，特别是在混合交通场景中理解人类驾驶员行为，辅助决策制定。此外，还可用于驾驶员行为分析和培训，提升驾驶安全。

## 📄 摘要（原文）

> Predicting driver attention is a critical problem for developing explainable autonomous driving systems and understanding driver behavior in mixed human-autonomous vehicle traffic scenarios. Although significant progress has been made through large-scale driver attention datasets and deep learning architectures, existing works are constrained by narrow frontal field-of-view and limited driving diversity. Consequently, they fail to capture the full spatial context of driving environments, especially during lane changes, turns, and interactions involving peripheral objects such as pedestrians or cyclists. In this paper, we introduce DriverGaze360, a large-scale 360$^\circ$ field of view driver attention dataset, containing $\sim$1 million gaze-labeled frames collected from 19 human drivers, enabling comprehensive omnidirectional modeling of driver gaze behavior. Moreover, our panoramic attention prediction approach, DriverGaze360-Net, jointly learns attention maps and attended objects by employing an auxiliary semantic segmentation head. This improves spatial awareness and attention prediction across wide panoramic inputs. Extensive experiments demonstrate that DriverGaze360-Net achieves state-of-the-art attention prediction performance on multiple metrics on panoramic driving images. Dataset and method available at https://av.dfki.de/drivergaze360.

