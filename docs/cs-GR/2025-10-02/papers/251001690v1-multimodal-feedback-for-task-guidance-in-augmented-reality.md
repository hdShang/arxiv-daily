---
layout: default
title: Multimodal Feedback for Task Guidance in Augmented Reality
---

# Multimodal Feedback for Task Guidance in Augmented Reality

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.01690" target="_blank" class="toolbar-btn">arXiv: 2510.01690v1</a>
    <a href="https://arxiv.org/pdf/2510.01690.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01690v1" 
            onclick="toggleFavorite(this, '2510.01690v1', 'Multimodal Feedback for Task Guidance in Augmented Reality')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Hu Guo, Lily Patel, Rohan Gupt

**分类**: cs.GR, cs.HC

**发布日期**: 2025-10-02

---

## 💡 一句话要点

**提出结合触觉反馈的增强现实任务指导方法，提升空间精度和可用性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `增强现实` `多模态反馈` `触觉反馈` `任务指导` `人机交互`

## 📋 核心要点

1. 现有OST-AR任务指导依赖视觉信息，易导致注意力过载，且在遮挡或光照不佳时深度感知受限。
2. 该研究提出一种结合OST-AR与腕式振动触觉的多模态反馈方法，以提升空间精度和可用性。
3. 实验结果表明，多模态反馈在认知负荷下能准确识别触觉模式，并优于仅视觉或仅触觉的指导。

## 📝 摘要（中文）

光学透视增强现实（OST-AR）将数字目标和注释叠加在物理世界上，为诸如医疗针头插入或组装等实践任务提供有前景的指导。最近关于OST-AR深度感知的研究表明，目标不透明度和工具可视化显著影响准确性和可用性；不透明目标和渲染真实工具可以减少深度误差，而透明目标和缺少工具会降低性能。然而，依赖视觉叠加可能会使注意力过载，并且当遮挡或光照阻碍感知时，几乎没有深度线索的空间。为了解决这些限制，我们探索了结合OST-AR与腕式振动触觉的多模态反馈。我们设计了一个带有六个振动马达的定制腕带，用于传递方向和状态提示，将其与手持工具和OST-AR集成，并评估其对提示识别和深度指导的影响。通过一项形成性研究和两项实验（N=21和N=27），我们表明参与者在认知负荷下准确地识别触觉模式，并且与仅视觉或仅触觉条件相比，多模态反馈提高了空间精度和可用性。

## 🔬 方法详解

**问题定义**：现有OST-AR任务指导主要依赖视觉信息，存在以下痛点：一是视觉信息过载，导致用户注意力分散；二是当存在遮挡或光照条件不佳时，深度感知能力下降，影响任务执行的准确性。因此，需要一种新的方法来增强AR任务指导的有效性和鲁棒性。

**核心思路**：该论文的核心思路是将视觉增强现实与触觉反馈相结合，利用腕式振动触觉提供额外的空间信息和状态提示。通过多模态融合，减轻视觉负担，增强用户对目标位置和状态的感知，从而提高任务执行的精度和效率。这种设计旨在克服纯视觉AR的局限性，提供更自然和直观的任务指导。

**技术框架**：整体框架包含三个主要组成部分：1) 光学透视增强现实（OST-AR）系统，用于在物理世界中叠加数字目标和注释；2) 定制腕带，配备六个振动马达，用于提供方向和状态提示；3) 手持工具，与腕带和OST-AR系统集成，用于执行实际任务。用户通过OST-AR系统观察虚拟目标，同时接收来自腕带的触觉反馈，从而获得更全面的任务指导。

**关键创新**：该论文的关键创新在于将腕式振动触觉反馈引入到OST-AR任务指导中，并设计了一种定制的腕带设备。这种多模态融合方法能够有效减轻视觉负担，增强用户对空间信息的感知，从而提高任务执行的精度和可用性。与传统的纯视觉AR指导相比，该方法具有更强的鲁棒性和适应性。

**关键设计**：定制腕带配备六个振动马达，通过不同的振动模式组合来传递方向和状态提示。具体的设计细节包括：1) 振动模式的选择，需要考虑用户的感知能力和认知负荷；2) 振动强度的调节，以确保用户能够清晰地感知到触觉反馈，同时避免过度刺激；3) 触觉反馈与视觉信息的同步，以提供一致和协调的任务指导。

## 📊 实验亮点

实验结果表明，参与者在认知负荷下能够准确识别触觉模式，并且与仅视觉或仅触觉条件相比，多模态反馈显著提高了空间精度和可用性。具体来说，多模态反馈在深度指导任务中表现出更高的精度，并且用户对多模态反馈的满意度也更高。实验结果验证了多模态反馈在增强现实任务指导中的有效性。

## 🎯 应用场景

该研究成果可应用于医疗、制造、维修等需要精确操作的任务指导场景。例如，在医疗领域，可用于辅助医生进行微创手术或针头穿刺；在制造领域，可用于指导工人进行复杂装配操作；在维修领域，可用于帮助技术人员进行设备故障排除和维修。通过提供更直观和高效的任务指导，提高工作效率和安全性。

## 📄 摘要（原文）

> Optical see-through augmented reality (OST-AR) overlays digital targets and annotations on the physical world, offering promising guidance for hands-on tasks such as medical needle insertion or assembly. Recent work on OST-AR depth perception shows that target opacity and tool visualization significantly affect accuracy and usability; opaque targets and rendering the real instrument reduce depth errors, whereas transparent targets and absent tools impair performance. However, reliance on visual overlays may overload attention and leaves little room for depth cues when occlusion or lighting hampers perception. To address these limitations, we explore multimodal feedback that combines OST-AR with wrist-based vibrotactile haptics. The past two years have seen rapid advances in haptic technology. Researchers have investigated skin-stretch and vibrotactile cues for conveying spatial information to blind users, wearable ring actuators that support precise pinching in AR, cross-modal audio-haptic cursors that enable eyes-free object selection, and wrist-worn feedback for teleoperated surgery that improves force awareness at the cost of longer task times. Studies comparing pull versus push vibrotactile metaphors found that pull cues yield faster gesture completion and lower cognitive load. These findings motivate revisiting OST-AR guidance with a fresh perspective on wrist-based haptics. We design a custom wristband with six vibromotors delivering directional and state cues, integrate it with a handheld tool and OST-AR, and assess its impact on cue recognition and depth guidance. Through a formative study and two experiments (N=21 and N=27), we show that participants accurately identify haptic patterns under cognitive load and that multimodal feedback improves spatial precision and usability compared with visual-only or haptic-only conditions.

