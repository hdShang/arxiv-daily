---
layout: default
title: "Beyond Sensor Data: Foundation Models of Behavioral Data from Wearables Improve Health Predictions"
---

# Beyond Sensor Data: Foundation Models of Behavioral Data from Wearables Improve Health Predictions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00191" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00191v1</a>
  <a href="https://arxiv.org/pdf/2507.00191.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00191v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00191v1', 'Beyond Sensor Data: Foundation Models of Behavioral Data from Wearables Improve Health Predictions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eray Erturk, Fahad Kamran, Salar Abbaspourazad, Sean Jewell, Harsh Sharma, Yujie Li, Sinead Williamson, Nicholas J Foti, Joseph Futoma

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-30

**备注**: Accepted to ICML 2025

---

## 💡 一句话要点

**提出行为数据基础模型以提升健康预测准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可穿戴设备` `健康预测` `基础模型` `行为数据` `深度学习` `个性化医疗` `数据优化`

## 📋 核心要点

1. 现有方法主要集中在低级传感器数据上，未能充分利用行为数据的潜在信息，导致健康预测的准确性不足。
2. 本文提出了一种新的基础模型，专注于行为信号，通过优化架构和标记策略，充分挖掘可穿戴设备数据的价值。
3. 在57个健康相关任务中，该模型表现优异，尤其在睡眠预测等行为驱动任务中，结合传感器数据后进一步提升了预测性能。

## 📝 摘要（中文）

可穿戴设备记录的生理和行为信号能够改善健康预测。尽管基础模型在健康预测中越来越多地被应用，但主要集中在低级传感器数据上，而行为数据因其与生理相关时间尺度和量的对齐，通常更具信息量。本文利用来自16.2万人的25亿小时可穿戴数据，开发了行为信号的基础模型，并系统优化了架构和标记策略。在57个健康相关任务上的评估显示，该模型在个体分类和时间变化健康状态预测等多种实际应用中表现出色，尤其在睡眠预测等行为驱动任务中表现优异，并在结合原始传感器数据表示后进一步提升。这些结果强调了针对可穿戴设备设计基础模型的重要性，并展示了启用新健康应用的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有健康预测模型对低级传感器数据的依赖，未能充分利用行为数据的不足。行为数据通常与生理相关的时间尺度和量更为一致，具有更高的信息价值。

**核心思路**：论文的核心思路是开发专门针对行为信号的基础模型，通过系统优化模型架构和标记策略，提升健康预测的准确性和实用性。

**技术框架**：整体架构包括数据收集、预处理、模型训练和评估四个主要阶段。数据收集阶段利用来自162K个个体的可穿戴设备数据，预处理阶段则对数据进行清洗和标记，模型训练阶段采用优化的深度学习架构，评估阶段则通过57个健康相关任务进行性能验证。

**关键创新**：最重要的技术创新点在于将行为数据与基础模型结合，系统优化了模型架构和标记策略，显著提升了模型在健康预测任务中的表现。这与传统方法的本质区别在于，传统方法往往忽视了行为数据的潜力。

**关键设计**：在模型设计中，采用了多层次的神经网络架构，结合了自注意力机制和卷积层，损失函数则根据任务类型进行了调整，以确保模型在不同健康预测任务中的适应性和准确性。

## 📊 实验亮点

在57个健康相关任务的评估中，模型在个体分类和时间变化健康状态预测方面表现出色，尤其在睡眠预测任务中，性能显著优于传统方法，结合传感器数据后进一步提升了预测准确性，展示了模型的广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括个体健康监测、慢性病管理和个性化医疗等。通过更准确的健康预测，能够帮助医疗专业人员制定更有效的干预措施，提高患者的健康管理水平，未来可能推动健康科技的进一步发展。

## 📄 摘要（原文）

> Wearable devices record physiological and behavioral signals that can improve health predictions. While foundation models are increasingly used for such predictions, they have been primarily applied to low-level sensor data, despite behavioral data often being more informative due to their alignment with physiologically relevant timescales and quantities. We develop foundation models of such behavioral signals using over 2.5B hours of wearable data from 162K individuals, systematically optimizing architectures and tokenization strategies for this unique dataset. Evaluated on 57 health-related tasks, our model shows strong performance across diverse real-world applications including individual-level classification and time-varying health state prediction. The model excels in behavior-driven tasks like sleep prediction, and improves further when combined with representations of raw sensor data. These results underscore the importance of tailoring foundation model design to wearables and demonstrate the potential to enable new health applications.

