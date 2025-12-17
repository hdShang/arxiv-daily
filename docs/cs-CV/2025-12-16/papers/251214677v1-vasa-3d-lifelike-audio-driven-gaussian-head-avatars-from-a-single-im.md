---
layout: default
title: VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image
---

# VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image

**arXiv**: [2512.14677v1](https://arxiv.org/abs/2512.14677) | [PDF](https://arxiv.org/pdf/2512.14677.pdf)

**作者**: Sicheng Xu, Guojun Chen, Jiaolong Yang, Yizhong Zhang, Yu Deng, Steve Lin, Baining Guo

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: NeurIPS 2025 paper. Project webpage: https://www.microsoft.com/en-us/research/project/vasa-3d/

---

## 💡 一句话要点

**提出VASA-3D，通过单张图像生成音频驱动的逼真3D头部化身，解决表情细节建模和单图重建挑战。**

**关键词**: `音频驱动生成` `3D头部化身` `单图像重建` `运动潜在表示` `优化框架` `自由视角视频` `实时渲染` `表情建模`

## 📋 核心要点

1. 现有方法难以从单张图像重建复杂3D头部化身，且表情细节建模不足，限制了真实感。
2. VASA-3D利用VASA-1的运动潜在表示，设计条件化3D模型，通过优化框架实现单图定制化。
3. 实验生成逼真3D说话头部，支持在线75 FPS自由视角视频，显著提升沉浸感和实时性能。

## 📝 摘要（中文）

我们提出了VASA-3D，一种音频驱动的单次3D头部化身生成器。这项研究解决了两个主要挑战：捕捉真实人脸的微妙表情细节，以及从单张肖像图像重建复杂的3D头部化身。为了准确建模表情细节，VASA-3D利用了VASA-1的运动潜在表示，该方法在2D说话头部生成中展现出卓越的真实感和生动性。我们工作的一个关键要素是将这种运动潜在表示转换到3D，这是通过设计一个以运动潜在为条件的3D头部模型来实现的。该模型针对单张图像的定制化是通过一个优化框架实现的，该框架使用了从输入图像合成的参考头部的大量视频帧。优化过程采用了多种训练损失，这些损失对生成训练数据中的伪影和有限姿态覆盖具有鲁棒性。我们的实验表明，VASA-3D生成了现有技术无法实现的逼真3D说话头部，并支持在线生成512x512自由视角视频，帧率高达75 FPS，从而促进了与逼真3D化身更沉浸式的互动。

## 🔬 方法详解

VASA-3D的整体框架基于音频驱动的3D头部化身生成，核心创新点包括：利用VASA-1的运动潜在表示来建模表情细节，设计一个以该运动潜在为条件的3D头部模型，实现从2D到3D的转换。关键技术创新在于通过优化框架定制化模型，使用从输入图像合成的视频帧进行训练，并采用鲁棒损失函数处理数据中的伪影和姿态限制。与现有方法的主要区别在于结合了2D说话头部的先进运动建模能力，并扩展到3D领域，解决了单图重建和表情细节的挑战，避免了传统方法对多视图数据或复杂采集的依赖。

## 📊 实验亮点

VASA-3D生成逼真3D说话头部，超越现有技术，支持在线生成512x512自由视角视频，帧率达75 FPS，实验验证了其在表情细节和实时性能上的显著提升。

## 🎯 应用场景

该研究在虚拟现实、增强现实、远程会议和娱乐领域具有广泛应用潜力，可生成逼真3D化身用于沉浸式交互、个性化虚拟角色和实时通信，提升用户体验和真实感。

## 📄 摘要（原文）

> We propose VASA-3D, an audio-driven, single-shot 3D head avatar generator. This research tackles two major challenges: capturing the subtle expression details present in real human faces, and reconstructing an intricate 3D head avatar from a single portrait image. To accurately model expression details, VASA-3D leverages the motion latent of VASA-1, a method that yields exceptional realism and vividness in 2D talking heads. A critical element of our work is translating this motion latent to 3D, which is accomplished by devising a 3D head model that is conditioned on the motion latent. Customization of this model to a single image is achieved through an optimization framework that employs numerous video frames of the reference head synthesized from the input image. The optimization takes various training losses robust to artifacts and limited pose coverage in the generated training data. Our experiment shows that VASA-3D produces realistic 3D talking heads that cannot be achieved by prior art, and it supports the online generation of 512x512 free-viewpoint videos at up to 75 FPS, facilitating more immersive engagements with lifelike 3D avatars.

