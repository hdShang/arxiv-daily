---
layout: default
title: Adaptive Event Stream Slicing for Open-Vocabulary Event-Based Object Detection via Vision-Language Knowledge Distillation
---

# Adaptive Event Stream Slicing for Open-Vocabulary Event-Based Object Detection via Vision-Language Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00681" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00681v1</a>
  <a href="https://arxiv.org/pdf/2510.00681.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00681v1" onclick="toggleFavorite(this, '2510.00681v1', 'Adaptive Event Stream Slicing for Open-Vocabulary Event-Based Object Detection via Vision-Language Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinchang Zhang, Zijun Li, Jiakai Lin, Guoyu Lu

**分类**: cs.CV

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**提出自适应事件流切片与知识蒸馏框架，实现开放词汇事件相机目标检测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `事件相机` `开放词汇目标检测` `知识蒸馏` `视觉-语言模型` `脉冲神经网络` `自适应事件流切片` `事件数据处理`

## 📋 核心要点

1. 现有事件相机目标检测方法依赖预定义类别，泛化能力弱，难以检测新物体。
2. 提出事件-图像知识蒸馏框架，利用CLIP的视觉知识指导事件相机目标检测模型训练。
3. 设计混合SNN和CNN架构，自适应事件流切片，保留关键时间信息，提升检测性能。

## 📝 摘要（中文）

事件相机因其高速响应、低延迟和对运动模糊的鲁棒性，在目标检测任务中具有优势。然而，事件相机缺乏纹理和颜色信息，使得开放词汇检测更具挑战性。现有的基于事件的检测方法通常在预定义的类别上进行训练，限制了它们对新物体的泛化能力，而遇到以前未见过的物体是很常见的。视觉-语言模型（VLM）已经实现了RGB图像中的开放词汇目标检测。然而，图像和事件流之间的模态差距使得直接将CLIP迁移到事件数据上是无效的，因为CLIP不是为事件流设计的。为了弥合这一差距，我们提出了一个事件-图像知识蒸馏框架，该框架利用CLIP的语义理解来实现事件数据的开放词汇目标检测。我们没有直接在事件流上训练CLIP，而是使用图像帧作为教师模型的输入，引导基于事件的学生模型学习CLIP丰富的视觉表示。通过基于空间注意力的蒸馏，学生网络直接从原始事件输入中学习有意义的视觉特征，同时继承CLIP广泛的视觉知识。此外，为了防止事件数据分割造成的信息丢失，我们设计了一个混合脉冲神经网络（SNN）和卷积神经网络（CNN）框架。与固定的事件分割方法（通常会丢弃关键的时间信息）不同，我们的SNN自适应地确定最佳的事件分割时刻，确保提取关键的时间特征。提取的事件特征随后由CNN处理以进行目标检测。

## 🔬 方法详解

**问题定义**：论文旨在解决事件相机在开放词汇目标检测中的挑战。现有方法通常在预定义的类别上训练，无法有效检测未见过的物体。直接将为RGB图像设计的视觉-语言模型（如CLIP）应用于事件数据效果不佳，因为事件数据缺乏纹理和颜色信息，存在模态差异。此外，传统的事件数据分割方法可能会丢失重要的时间信息。

**核心思路**：论文的核心思路是利用知识蒸馏，将视觉-语言模型CLIP的知识迁移到事件相机数据上。通过将RGB图像作为教师模型的输入，引导事件相机学生模型学习CLIP的视觉表示，从而弥合模态差距。同时，采用自适应事件流切片方法，保留关键的时间信息，提升检测性能。

**技术框架**：整体框架包含两个主要部分：知识蒸馏和自适应事件流处理。首先，使用RGB图像训练CLIP模型作为教师模型。然后，将事件数据输入到学生模型中，学生模型通过空间注意力机制学习教师模型的视觉表示。同时，使用混合SNN和CNN架构处理事件流，SNN负责自适应地分割事件流，提取关键的时间特征，CNN负责目标检测。

**关键创新**：论文的关键创新在于：1) 提出了一种事件-图像知识蒸馏框架，有效地将CLIP的知识迁移到事件相机数据上，实现了开放词汇目标检测。2) 设计了一种混合SNN和CNN架构，能够自适应地分割事件流，保留关键的时间信息，避免了传统固定分割方法的信息丢失。

**关键设计**：在知识蒸馏过程中，采用了空间注意力机制，使得学生模型能够关注图像中的关键区域，从而更好地学习教师模型的视觉表示。SNN的设计允许网络根据事件的动态特性自适应地调整分割时刻，而不是采用固定的时间窗口。损失函数的设计可能包括分类损失、回归损失以及知识蒸馏损失，以确保学生模型能够准确地检测目标并学习教师模型的知识。具体的网络结构参数和损失函数权重等细节可能在论文中有更详细的描述。

## 📊 实验亮点

论文提出了一种新颖的事件相机开放词汇目标检测框架，通过知识蒸馏和自适应事件流切片，有效提升了检测性能。具体的实验结果（例如，在特定数据集上的mAP提升）需要在论文中查找。与现有基于事件的检测方法相比，该方法在检测新物体方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、安防监控等领域。在这些场景中，事件相机能够提供高速、低延迟的视觉信息，尤其是在光线不足或快速运动的情况下。开放词汇目标检测能力使得系统能够识别各种未知的物体，提高了系统的鲁棒性和适应性。未来，该技术有望进一步提升智能系统的感知能力，使其能够更好地理解和适应复杂环境。

## 📄 摘要（原文）

> Event cameras offer advantages in object detection tasks due to high-speed response, low latency, and robustness to motion blur. However, event cameras lack texture and color information, making open-vocabulary detection particularly challenging. Current event-based detection methods are typically trained on predefined categories, limiting their ability to generalize to novel objects, where encountering previously unseen objects is common. Vision-language models (VLMs) have enabled open-vocabulary object detection in RGB images. However, the modality gap between images and event streams makes it ineffective to directly transfer CLIP to event data, as CLIP was not designed for event streams. To bridge this gap, we propose an event-image knowledge distillation framework that leverages CLIP's semantic understanding to achieve open-vocabulary object detection on event data. Instead of training CLIP directly on event streams, we use image frames as inputs to a teacher model, guiding the event-based student model to learn CLIP's rich visual representations. Through spatial attention-based distillation, the student network learns meaningful visual features directly from raw event inputs while inheriting CLIP's broad visual knowledge. Furthermore, to prevent information loss due to event data segmentation, we design a hybrid spiking neural network (SNN) and convolutional neural network (CNN) framework. Unlike fixed-group event segmentation methods, which often discard crucial temporal information, our SNN adaptively determines the optimal event segmentation moments, ensuring that key temporal features are extracted. The extracted event features are then processed by CNNs for object detection.

