---
layout: default
title: OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation
---

# OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01210" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01210v2</a>
  <a href="https://arxiv.org/pdf/2511.01210.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01210v2" onclick="toggleFavorite(this, '2511.01210v2', 'OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heyu Guo, Shanmu Wang, Ruichun Ma, Shiqi Jiang, Yasaman Ghasempour, Omid Abari, Baining Guo, Lili Qiu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-03 (更新: 2025-11-06)

---

## 💡 一句话要点

**OmniVLA：面向机器人操作的物理 grounding 多模态 VLA 模型，统一多传感器感知**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多模态融合` `机器人操作` `视觉语言动作` `传感器融合` `物理 grounding`

## 📋 核心要点

1. 现有VLA模型主要依赖RGB相机，感知能力受限，难以应对复杂操作任务。
2. OmniVLA通过传感器掩码图像统一表示多模态信息，实现物理 grounding 的空间智能。
3. 实验表明，OmniVLA在真实机器人操作任务中显著优于RGB-only和原始传感器输入模型。

## 📝 摘要（中文）

视觉-语言-动作 (VLA) 模型通过大规模视觉-语言预训练，在机器人动作预测方面表现出强大的泛化能力。然而，现有模型大多仅依赖 RGB 相机，限制了其感知和操作能力。我们提出了 OmniVLA，一个全模态 VLA 模型，集成了新的传感模态，以实现超越 RGB 感知的物理 grounding 空间智能。我们的核心方法是传感器掩码图像，一种统一的表示，将来自红外相机、毫米波雷达和麦克风阵列等传感器的空间 grounding 和物理意义的掩码叠加到 RGB 图像上。这种图像原生的统一保持了传感器输入接近 RGB 统计，便于训练，提供了跨传感器硬件的统一接口，并通过轻量级的每传感器投影器实现数据高效学习。在此基础上，我们提出了一个多传感器视觉-语言-动作模型架构，并基于 RGB 预训练的 VLA 主干网络训练模型。我们在具有挑战性的真实世界任务中评估了 OmniVLA，其中传感器模态感知指导机器人操作。OmniVLA 实现了 84% 的平均任务成功率，显著优于仅使用 RGB 和原始传感器输入的基线模型，分别提高了 59% 和 28%，同时显示出更高的学习效率和更强的泛化能力。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型在机器人操作任务中，主要依赖RGB相机获取视觉信息，这限制了模型对环境的感知能力，尤其是在光照变化、遮挡等情况下。现有方法难以有效融合多种传感器信息，导致模型泛化能力不足。

**核心思路**：OmniVLA的核心思路是将来自不同传感器的信息（如红外相机、毫米波雷达、麦克风阵列）统一表示为“传感器掩码图像”，并叠加到RGB图像上。这种方法保持了传感器输入与RGB图像的统计相似性，便于模型训练，并提供了一个统一的传感器接口。

**技术框架**：OmniVLA的整体架构包括以下几个主要模块：1) 多传感器数据采集模块，负责采集来自不同传感器的原始数据；2) 传感器掩码图像生成模块，将原始传感器数据转换为空间 grounding 的掩码图像；3) 多模态融合模块，将传感器掩码图像叠加到RGB图像上，形成统一的输入表示；4) VLA模型，基于RGB预训练的VLA主干网络，对多模态输入进行处理，预测机器人动作。

**关键创新**：OmniVLA最重要的技术创新点在于“传感器掩码图像”的统一表示方法。这种方法将不同类型的传感器数据转换为图像形式，使其能够与RGB图像进行有效融合，同时保留了传感器数据的物理意义和空间信息。与直接使用原始传感器数据相比，这种方法更易于训练，并具有更好的泛化能力。

**关键设计**：OmniVLA的关键设计包括：1) 轻量级的每传感器投影器，用于将原始传感器数据转换为传感器掩码图像；2) 基于RGB预训练的VLA主干网络，利用大规模RGB图像数据进行预训练，提高模型的泛化能力；3) 针对机器人操作任务设计的损失函数，用于优化模型的动作预测性能。

## 📊 实验亮点

OmniVLA在真实机器人操作任务中取得了显著的性能提升。实验结果表明，OmniVLA的平均任务成功率达到84%，相比于仅使用RGB的基线模型提高了59%，相比于使用原始传感器输入的基线模型提高了28%。同时，OmniVLA还表现出更高的学习效率和更强的泛化能力。

## 🎯 应用场景

OmniVLA可应用于各种需要多模态感知和精确操作的机器人应用场景，如智能制造、家庭服务机器人、医疗机器人和自动驾驶等。通过融合多种传感器信息，OmniVLA能够提高机器人在复杂环境中的适应性和操作精度，实现更安全、更高效的自动化。

## 📄 摘要（原文）

> Vision-language-action (VLA) models have shown strong generalization for robotic action prediction through large-scale vision-language pretraining. However, most existing models rely solely on RGB cameras, limiting their perception and, consequently, manipulation capabilities. We present OmniVLA, an omni-modality VLA model that integrates novel sensing modalities for physically-grounded spatial intelligence beyond RGB perception. The core of our approach is the sensor-masked image, a unified representation that overlays spatially grounded and physically meaningful masks onto the RGB images, derived from sensors including an infrared camera, a mmWave radar, and a microphone array. This image-native unification keeps sensor input close to RGB statistics to facilitate training, provides a uniform interface across sensor hardware, and enables data-efficient learning with lightweight per-sensor projectors. Built on this, we present a multisensory vision-language-action model architecture and train the model based on an RGB-pretrained VLA backbone. We evaluate OmniVLA on challenging real-world tasks where sensor-modality perception guides the robotic manipulation. OmniVLA achieves an average task success rate of 84%, significantly outperforms both RGB-only and raw-sensor-input baseline models by 59% and 28% respectively, meanwhile showing higher learning efficiency and stronger generalization capability.

