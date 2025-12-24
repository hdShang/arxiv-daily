---
layout: default
title: Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting
---

# Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20014" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20014v1</a>
  <a href="https://arxiv.org/pdf/2512.20014.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20014v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20014v1', 'Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sangoh Lee, Sangwoo Mo, Wook-Shin Han

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出视觉注意力提示（VAP），解决VLA模型在个性化指令下的物体操作难题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `个性化指令` `视觉注意力提示` `机器人操作` `物体识别`

## 📋 核心要点

1. VLA模型在处理个性化指令时，难以区分视觉相似但属于不同用户的物体，导致操作失败。
2. VAP通过将参考图像作为视觉记忆，利用开放词汇检测和嵌入匹配来定位目标物体，并将其作为视觉提示注入VLA模型。
3. 在模拟和真实环境的实验中，VAP显著提高了成功率和正确物体操作率，优于现有方法。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型在通用指令上表现良好，但在个性化指令（如“拿我的杯子”）中表现不佳，因为机器人必须在视觉上相似的物体中操作特定实例。本文研究了操作个人物品的场景，其中VLA模型必须仅使用少量参考图像来识别和控制训练期间未见过的用户特定对象。为了解决这个挑战，我们提出了视觉注意力提示（VAP），这是一种简单而有效的免训练感知适配器，它为冻结的VLA模型配备了自上而下的选择性注意力。VAP将参考图像视为非参数视觉记忆，通过开放词汇检测和基于嵌入的匹配将个人对象定位在场景中，然后通过突出显示对象并重写指令，将此定位作为视觉提示注入。我们构建了两个模拟基准（Personalized-SIMPLER和Personalized-VLABench）和一个真实世界的桌面基准，以评估跨多个机器人和任务的个性化操作。实验表明，VAP在成功率和正确对象操作方面始终优于通用策略和token-learning基线，有助于弥合语义理解和实例级控制之间的差距。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作（VLA）模型在处理通用指令时表现良好，但当需要操作特定用户的物品时，例如“把我的杯子拿过来”，由于视觉上相似的物体很多，模型难以区分并正确操作目标物体。现有方法缺乏对用户个性化信息的有效利用，导致泛化能力不足。

**核心思路**：本文的核心思路是将用户的参考图像作为视觉记忆，通过视觉注意力机制引导VLA模型关注目标物体。具体来说，VAP利用参考图像来定位场景中的目标物体，并将定位结果作为视觉提示，增强VLA模型对个性化指令的理解和执行能力。这种方法无需重新训练VLA模型，即可实现个性化操作。

**技术框架**：VAP主要包含三个阶段：1) **物体定位**：利用开放词汇检测器和基于嵌入的匹配方法，将参考图像中的目标物体定位到当前场景中。2) **视觉提示生成**：根据物体定位结果，生成视觉提示，例如突出显示目标物体。3) **指令重写**：将原始指令与视觉提示相结合，生成新的指令，输入到VLA模型中。VLA模型根据新的指令执行相应的动作。

**关键创新**：VAP的关键创新在于提出了一种免训练的感知适配器，通过视觉注意力提示的方式，将用户的个性化信息注入到冻结的VLA模型中。与传统的微调方法相比，VAP无需重新训练模型，降低了计算成本和数据需求。此外，VAP利用开放词汇检测器和嵌入匹配方法，实现了对未知物体的定位和操作。

**关键设计**：VAP的关键设计包括：1) 使用CLIP模型提取图像和文本的嵌入向量，用于计算物体之间的相似度。2) 利用注意力机制，根据参考图像和场景图像的相似度，生成视觉注意力图。3) 通过突出显示目标物体的方式，生成视觉提示。4) 将视觉提示与原始指令拼接，生成新的指令。具体参数设置和损失函数细节在论文中未明确说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20014v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20014v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20014v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，VAP在Personalized-SIMPLER、Personalized-VLABench和真实世界桌面基准测试中，均显著优于通用策略和token-learning基线。具体而言，VAP在成功率和正确对象操作方面均取得了显著提升，表明其能够有效解决VLA模型在个性化指令下的物体操作难题。具体提升幅度在论文中未给出明确数据，属于未知信息。

## 🎯 应用场景

该研究成果可应用于家庭服务机器人、智能助手等领域，使机器人能够更好地理解和执行用户的个性化指令，例如识别并拿取用户的特定物品、根据用户的偏好调整环境设置等。这项技术有助于提升人机交互的自然性和效率，增强用户体验，并为机器人更广泛的应用奠定基础。

## 📄 摘要（原文）

> While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup", where the robot must act on one specific instance among visually similar objects. We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images. To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with top-down selective attention. VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then injects this grounding as a visual prompt by highlighting the object and rewriting the instruction. We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipulation across multiple robots and tasks. Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level control.

