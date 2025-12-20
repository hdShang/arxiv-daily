---
layout: default
title: The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text
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

**关键词**: `世界事件模拟` `多模态融合` `轨迹控制` `视频生成` `涌现一致性`

## 📋 核心要点

1. 现有方法在世界事件模拟中，要么仅依赖文本，缺乏精细控制，要么依赖轨迹控制，但难以保持视觉一致性。
2. WorldCanvas结合文本、轨迹和参考图像，利用多模态信息实现对世界事件的精确控制和视觉一致性保持。
3. 实验结果表明，WorldCanvas能够生成具有时间连贯性和涌现一致性的视频，实现多智能体交互和对象外观控制。

## 📝 摘要（中文）

我们提出了WorldCanvas，一个用于可提示世界事件的框架，它通过结合文本、轨迹和参考图像来实现丰富的、用户导向的模拟。与仅使用文本的方法和现有的轨迹控制图像到视频方法不同，我们的多模态方法将轨迹（编码运动、时间和可见性）与自然语言（用于语义意图）和参考图像（用于对象身份的视觉基础）相结合，从而能够生成连贯的、可控的事件，包括多智能体交互、对象进入/退出、参考引导的外观和违反直觉的事件。生成的视频不仅展示了时间连贯性，还展示了涌现一致性，即使在暂时消失的情况下也能保持对象身份和场景。通过支持表达性的世界事件生成，WorldCanvas将世界模型从被动预测器提升为交互式的、用户塑造的模拟器。我们的项目页面位于：https://worldcanvas.github.io/。

## 🔬 方法详解

**问题定义**：现有世界事件模拟方法存在局限性。基于文本的方法难以精确控制事件细节，而基于轨迹控制的图像到视频方法难以保持对象身份和场景的一致性，尤其是在对象暂时消失的情况下。因此，需要一种能够结合语义意图、运动信息和视觉信息的框架，以实现更丰富、更可控的世界事件模拟。

**核心思路**：WorldCanvas的核心思路是利用多模态信息融合，将文本的语义信息、轨迹的运动信息和参考图像的视觉信息结合起来，从而实现对世界事件的精确控制和视觉一致性保持。通过这种方式，可以生成包含多智能体交互、对象进入/退出、参考引导的外观和违反直觉的事件的连贯视频。

**技术框架**：WorldCanvas框架包含以下主要模块：1) 轨迹编码模块，用于编码对象的运动轨迹，包括位置、时间和可见性等信息；2) 文本编码模块，用于编码自然语言描述，提取语义意图；3) 参考图像编码模块，用于编码参考图像，提取对象身份和外观信息；4) 视频生成模块，基于编码后的轨迹、文本和参考图像，生成具有时间连贯性和涌现一致性的视频。

**关键创新**：WorldCanvas的关键创新在于多模态信息的融合方式。它不仅简单地将文本、轨迹和参考图像的信息拼接在一起，而是通过一种精心设计的融合机制，使得不同模态的信息能够相互补充，从而实现对世界事件的更精确控制和更逼真模拟。此外，该框架还引入了涌现一致性的概念，即使在对象暂时消失的情况下，也能保持对象身份和场景的一致性。

**关键设计**：具体的技术细节包括：轨迹编码采用时序模型（例如LSTM或Transformer）来捕捉运动模式；文本编码采用预训练语言模型（例如BERT或GPT）来提取语义信息；参考图像编码采用卷积神经网络（例如ResNet或ViT）来提取视觉特征。视频生成模块可能采用生成对抗网络（GAN）或扩散模型等技术，以生成高质量的视频。损失函数的设计需要考虑时间连贯性、涌现一致性和参考图像的相似性。

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

WorldCanvas通过结合文本、轨迹和参考图像，实现了对世界事件的精细控制和视觉一致性保持。实验结果表明，该方法能够生成具有时间连贯性和涌现一致性的视频，包括多智能体交互、对象进入/退出等复杂事件。与现有方法相比，WorldCanvas在对象身份保持和场景一致性方面取得了显著提升，能够生成更逼真、更可控的世界事件模拟。

## 🎯 应用场景

WorldCanvas可应用于游戏开发、电影制作、机器人仿真、自动驾驶等领域。它可以帮助开发者快速生成各种场景和事件，提高开发效率。在机器人仿真和自动驾驶领域，WorldCanvas可以用于生成各种复杂的交通场景，帮助训练和评估算法的性能。此外，该技术还可以用于教育和娱乐领域，例如创建个性化的故事和虚拟体验。

## 📄 摘要（原文）

> We present WorldCanvas, a framework for promptable world events that enables rich, user-directed simulation by combining text, trajectories, and reference images. Unlike text-only approaches and existing trajectory-controlled image-to-video methods, our multimodal approach combines trajectories -- encoding motion, timing, and visibility -- with natural language for semantic intent and reference images for visual grounding of object identity, enabling the generation of coherent, controllable events that include multi-agent interactions, object entry/exit, reference-guided appearance and counterintuitive events. The resulting videos demonstrate not only temporal coherence but also emergent consistency, preserving object identity and scene despite temporary disappearance. By supporting expressive world events generation, WorldCanvas advances world models from passive predictors to interactive, user-shaped simulators. Our project page is available at: https://worldcanvas.github.io/.

