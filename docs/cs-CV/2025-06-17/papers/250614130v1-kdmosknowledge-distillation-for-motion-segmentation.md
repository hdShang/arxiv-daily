---
layout: default
title: "KDMOS:Knowledge Distillation for Motion Segmentation"
---

# KDMOS:Knowledge Distillation for Motion Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14130" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14130v1</a>
  <a href="https://arxiv.org/pdf/2506.14130.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14130v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14130v1', 'KDMOS:Knowledge Distillation for Motion Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chunyu Cao, Jintao Cheng, Zeyu Chen, Linfan Zhan, Rui Fan, Zhijian He, Xiaoyu Tang

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-06-17

**🔗 代码/项目**: [GITHUB](https://github.com/SCNU-RISLAB/KDMOS)

---

## 💡 一句话要点

**提出KDMOS以解决运动物体分割中的实时性与准确性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `运动物体分割` `知识蒸馏` `实时推理` `鸟瞰图` `深度学习` `网络优化` `自动驾驶`

## 📋 核心要点

1. 现有运动物体分割方法在准确性与实时推理之间难以取得平衡，导致在实际应用中存在局限性。
2. 本文提出了一种基于logits的知识蒸馏框架，通过解耦移动与非移动类，优化教师模型的学习效果。
3. 实验结果显示，本文方法在SemanticKITTI-MOS数据集上达到了78.8%的IoU，且参数量减少7.69%，有效缓解了过拟合问题。

## 📝 摘要（中文）

运动物体分割（MOS）在自动驾驶中至关重要，能够提升定位、路径规划、地图构建、场景流估计和未来状态预测的能力。尽管现有方法表现强劲，但在准确性与实时推理之间的平衡仍然是一个挑战。为此，本文提出了一种基于logits的知识蒸馏框架，旨在提高准确性同时保持实时效率。具体而言，我们采用基于鸟瞰图（BEV）投影的模型作为学生模型，非投影模型作为教师模型。为了解决移动类与非移动类之间的严重不平衡，我们对其进行解耦，并应用定制的蒸馏策略，使教师模型能够更好地学习关键的运动相关特征。该方法显著减少了假阳性和假阴性。此外，我们引入了动态上采样，优化了网络架构，实现了7.69%的参数减少，缓解了过拟合。我们的算法在SemanticKITTI-MOS数据集的隐藏测试集上达到了78.8%的IoU，并在Apollo数据集上取得了竞争性结果。

## 🔬 方法详解

**问题定义**：本文旨在解决运动物体分割中的准确性与实时性之间的矛盾。现有方法在处理移动与非移动类的不平衡时，往往导致较高的假阳性和假阴性率。

**核心思路**：我们提出了一种基于logits的知识蒸馏框架，采用鸟瞰图（BEV）投影模型作为学生模型，非投影模型作为教师模型，通过解耦移动与非移动类来优化学习效果。

**技术框架**：整体架构包括教师模型和学生模型的协同训练，教师模型负责提取运动相关特征，而学生模型则通过蒸馏策略进行学习。我们还引入了动态上采样和网络架构优化，以提升模型性能。

**关键创新**：最重要的创新在于定制的蒸馏策略和动态上采样技术，使得教师模型能够更有效地学习运动特征，从而显著降低假阳性和假阴性。

**关键设计**：在参数设置上，我们实现了7.69%的参数减少，采用了特定的损失函数来平衡移动与非移动类的学习，优化了网络结构以提升整体性能。通过这些设计，模型在准确性和效率上均有显著提升。

## 📊 实验亮点

在实验中，KDMOS方法在SemanticKITTI-MOS数据集的隐藏测试集上达到了78.8%的IoU，相较于基线方法显著提升。同时，通过优化网络架构，参数数量减少了7.69%，有效缓解了过拟合现象，展现了良好的实时性与准确性平衡。

## 🎯 应用场景

该研究在自动驾驶、智能监控和机器人导航等领域具有广泛的应用潜力。通过提高运动物体分割的准确性与实时性，能够显著提升自动驾驶系统的安全性与可靠性，推动智能交通的发展。此外，研究成果也可为其他需要实时处理动态场景的应用提供技术支持。

## 📄 摘要（原文）

> Motion Object Segmentation (MOS) is crucial for autonomous driving, as it enhances localization, path planning, map construction, scene flow estimation, and future state prediction. While existing methods achieve strong performance, balancing accuracy and real-time inference remains a challenge. To address this, we propose a logits-based knowledge distillation framework for MOS, aiming to improve accuracy while maintaining real-time efficiency. Specifically, we adopt a Bird's Eye View (BEV) projection-based model as the student and a non-projection model as the teacher. To handle the severe imbalance between moving and non-moving classes, we decouple them and apply tailored distillation strategies, allowing the teacher model to better learn key motion-related features. This approach significantly reduces false positives and false negatives. Additionally, we introduce dynamic upsampling, optimize the network architecture, and achieve a 7.69% reduction in parameter count, mitigating overfitting. Our method achieves a notable IoU of 78.8% on the hidden test set of the SemanticKITTI-MOS dataset and delivers competitive results on the Apollo dataset. The KDMOS implementation is available at https://github.com/SCNU-RISLAB/KDMOS.

