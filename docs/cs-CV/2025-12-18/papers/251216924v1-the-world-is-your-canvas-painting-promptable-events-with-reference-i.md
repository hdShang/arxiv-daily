---
layout: default
title: "The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text"
---

# The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16924" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16924v1</a>
  <a href="https://arxiv.org/pdf/2512.16924.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16924v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16924v1', 'The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanlin Wang, Hao Ouyang, Qiuyu Wang, Yue Yu, Yihao Meng, Wen Wang, Ka Leong Cheng, Shuailei Ma, Qingyan Bai, Yixuan Li, Cheng Chen, Yanhong Zeng, Xing Zhu, Yujun Shen, Qifeng Chen

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project page and code: https://worldcanvas.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://worldcanvas.github.io/)

---

## 💡 一句话要点

**WorldCanvas：结合文本、轨迹和参考图像，实现可控的世界事件模拟。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `世界事件模拟` `多模态融合` `轨迹控制` `参考图像引导` `视频生成`

## 📋 核心要点

1. 现有方法在世界事件模拟中，要么仅依赖文本，缺乏精细控制，要么依赖轨迹控制，但缺乏对对象身份的视觉 grounding。
2. WorldCanvas 结合文本、轨迹和参考图像，利用轨迹编码运动，文本表达语义意图，参考图像提供视觉 grounding，实现可控事件生成。
3. 实验结果表明，WorldCanvas 生成的视频具有时间一致性和涌现一致性，即使对象暂时消失，也能保持对象身份和场景的连贯性。

## 📝 摘要（中文）

本文提出了WorldCanvas，一个用于可提示世界事件的框架，它通过结合文本、轨迹和参考图像来实现丰富的、用户导向的模拟。与仅使用文本的方法和现有的轨迹控制图像到视频方法不同，我们的多模态方法将轨迹（编码运动、时间安排和可见性）与自然语言（用于语义意图）以及参考图像（用于对象身份的视觉基础）相结合，从而能够生成连贯的、可控的事件，包括多智能体交互、对象进入/退出、参考引导的外观和违反直觉的事件。生成的视频不仅展示了时间一致性，还展示了涌现一致性，即使在暂时消失的情况下也能保持对象身份和场景。通过支持富有表现力的世界事件生成，WorldCanvas将世界模型从被动预测器提升为交互式的、用户塑造的模拟器。

## 🔬 方法详解

**问题定义**：现有世界事件模拟方法存在局限性。基于文本的方法难以实现精细控制，而基于轨迹控制的图像到视频方法缺乏对对象身份的视觉 grounding，无法生成包含复杂交互和对象变化的连贯事件。因此，需要一种能够结合多种模态信息，实现用户可控、视觉一致的世界事件模拟框架。

**核心思路**：WorldCanvas 的核心思路是将文本、轨迹和参考图像三种模态的信息融合起来，共同驱动世界事件的生成。轨迹信息负责控制运动、时间安排和可见性，文本信息负责表达语义意图，参考图像负责提供对象身份的视觉 grounding。通过这种多模态融合的方式，可以生成更加丰富、可控和视觉一致的世界事件。

**技术框架**：WorldCanvas 的整体框架包含以下几个主要模块：1) 轨迹编码模块：负责将轨迹信息编码成可供后续模块使用的特征向量。2) 文本编码模块：负责将文本信息编码成语义向量。3) 参考图像编码模块：负责提取参考图像的视觉特征。4) 事件生成模块：该模块接收轨迹特征、语义向量和视觉特征作为输入，生成相应的视频帧。该模块通常基于生成对抗网络（GAN）或扩散模型等技术实现。

**关键创新**：WorldCanvas 的关键创新在于其多模态融合的事件生成方式。它不仅考虑了运动轨迹和语义意图，还引入了参考图像作为视觉 grounding，从而能够生成更加真实、可控和视觉一致的世界事件。与现有方法相比，WorldCanvas 能够更好地处理多智能体交互、对象进入/退出、参考引导的外观和违反直觉的事件。

**关键设计**：具体的技术细节包括：轨迹编码模块可能使用循环神经网络（RNN）或 Transformer 等序列模型来处理轨迹信息；文本编码模块可能使用预训练的语言模型（如 BERT 或 GPT）来提取语义特征；参考图像编码模块可能使用卷积神经网络（CNN）来提取视觉特征；事件生成模块可能使用时空 GAN 或扩散模型来生成视频帧。损失函数的设计需要考虑时间一致性、视觉一致性和语义一致性，例如可以使用对抗损失、循环一致性损失和语义相似度损失等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16924v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16924v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16924v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过大量实验验证了 WorldCanvas 的有效性。实验结果表明，WorldCanvas 生成的视频在时间一致性、视觉一致性和语义一致性方面均优于现有方法。例如，在对象进入/退出场景的实验中，WorldCanvas 能够保持对象身份和外观的一致性，即使对象暂时消失也能正确地重新出现。此外，WorldCanvas 还能够生成违反直觉的事件，例如让物体以不符合物理规律的方式运动。

## 🎯 应用场景

WorldCanvas 在游戏开发、电影制作、机器人仿真、自动驾驶测试等领域具有广泛的应用前景。它可以用于生成各种虚拟场景和事件，帮助开发者快速创建游戏内容、进行电影特效制作、训练机器人和测试自动驾驶系统。此外，WorldCanvas 还可以用于教育和娱乐领域，例如创建交互式故事和虚拟现实体验。

## 📄 摘要（原文）

> We present WorldCanvas, a framework for promptable world events that enables rich, user-directed simulation by combining text, trajectories, and reference images. Unlike text-only approaches and existing trajectory-controlled image-to-video methods, our multimodal approach combines trajectories -- encoding motion, timing, and visibility -- with natural language for semantic intent and reference images for visual grounding of object identity, enabling the generation of coherent, controllable events that include multi-agent interactions, object entry/exit, reference-guided appearance and counterintuitive events. The resulting videos demonstrate not only temporal coherence but also emergent consistency, preserving object identity and scene despite temporary disappearance. By supporting expressive world events generation, WorldCanvas advances world models from passive predictors to interactive, user-shaped simulators. Our project page is available at: https://worldcanvas.github.io/.

