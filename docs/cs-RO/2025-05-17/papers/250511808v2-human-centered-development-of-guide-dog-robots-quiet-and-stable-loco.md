---
layout: default
title: "Human-Centered Development of Guide Dog Robots: Quiet and Stable Locomotion Control"
---

# Human-Centered Development of Guide Dog Robots: Quiet and Stable Locomotion Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11808" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11808v2</a>
  <a href="https://arxiv.org/pdf/2505.11808.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11808v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11808v2', 'Human-Centered Development of Guide Dog Robots: Quiet and Stable Locomotion Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shangqun Yu, Hochul Hwang, Trung M. Dang, Joydeep Biswas, Nicholas A. Giudice, Sunghoon Ivan Lee, Donghyun Kim

**分类**: cs.RO, cs.HC

**发布日期**: 2025-05-17 (更新: 2025-05-27)

---

## 💡 一句话要点

**提出一种新型步态控制器以解决盲人导盲犬机器人运动噪音与不稳定性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `导盲犬机器人` `步态控制` `盲人辅助技术` `四足机器人` `平稳行走` `用户体验` `噪音减少`

## 📋 核心要点

1. 现有四足机器人在行走时产生的噪音和抖动问题，严重影响了盲人和低视力人士的使用体验。
2. 论文提出了一种新型步态控制器，旨在实现平稳的步态和稳定的平衡控制，以适应盲人用户的需求。
3. 实验结果表明，新控制器在噪音减少方面表现显著优于默认控制器，用户接受度也得到了提升。

## 📝 摘要（中文）

四足机器人因其形态与导盲犬相似，成为辅助盲人和低视力人士的有前景的系统。然而，现有四足机器人在行走时的噪音和抖动问题严重影响了其可靠性。通过与导盲犬训练师的访谈，我们发现这些干扰对依赖环境声音导航的盲人尤为困扰。为此，我们开发了一种新型步态控制器，旨在实现缓慢平稳的步态，同时保持人类的行走速度，并增强平衡控制。该控制器与感知系统集成，能够在不平坦的地形上行走。经过广泛测试，我们的控制器在噪音减少方面表现优异，噪音水平仅为默认控制器的一半。室内实验结果显示，参与者对新控制器的接受度显著高于默认控制器，表明其在导盲犬机器人用户体验方面的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有导盲犬机器人在行走过程中产生的噪音和抖动问题，这些问题会对盲人和低视力人士的导航造成干扰。现有方法未能有效考虑这些因素，导致用户体验不佳。

**核心思路**：我们提出了一种新型步态控制器，专注于实现缓慢而平稳的步态，同时保持与人类行走速度的匹配。通过优化步态控制，减少运动中的噪音和不稳定性，从而提升用户体验。

**技术框架**：该控制器由多个模块组成，包括步态生成模块、平衡控制模块和感知系统集成模块。步态生成模块负责生成平稳的步态，平衡控制模块确保机器人在行走过程中的稳定性，而感知系统则帮助机器人适应不平坦的地形。

**关键创新**：本研究的主要创新在于开发了一个能够显著降低运动噪音的步态控制器，其噪音水平仅为默认控制器的一半。这一创新使得机器人在行走时更加安静，减少了对盲人用户的干扰。

**关键设计**：控制器的设计中，关键参数包括步态频率、步幅和重心控制。我们采用了特定的损失函数来优化步态的平滑性，并通过实验调整了控制器的参数，以确保在不同地形上的稳定性和适应性。

## 📊 实验亮点

实验结果显示，新型步态控制器在噪音减少方面表现优异，噪音水平仅为默认控制器的一半。此外，参与者在室内行走实验中对新控制器的接受度显著提高，表明其在用户体验方面的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括盲人辅助技术、老年人移动辅助设备以及其他需要稳定行走的机器人系统。通过提高导盲犬机器人的可靠性和用户体验，未来有望在公共交通、家庭和户外环境中广泛应用，改善盲人和低视力人士的生活质量。

## 📄 摘要（原文）

> A quadruped robot is a promising system that can offer assistance comparable to that of dog guides due to its similar form factor. However, various challenges remain in making these robots a reliable option for blind and low-vision (BLV) individuals. Among these challenges, noise and jerky motion during walking are critical drawbacks of existing quadruped robots. While these issues have largely been overlooked in guide dog robot research, our interviews with guide dog handlers and trainers revealed that acoustic and physical disturbances can be particularly disruptive for BLV individuals, who rely heavily on environmental sounds for navigation. To address these issues, we developed a novel walking controller for slow stepping and smooth foot swing/contact while maintaining human walking speed, as well as robust and stable balance control. The controller integrates with a perception system to facilitate locomotion over non-flat terrains, such as stairs. Our controller was extensively tested on the Unitree Go1 robot and, when compared with other control methods, demonstrated significant noise reduction -- half of the default locomotion controller. In this study, we adopt a mixed-methods approach to evaluate its usability with BLV individuals. In our indoor walking experiments, participants compared our controller to the robot's default controller. Results demonstrated superior acceptance of our controller, highlighting its potential to improve the user experience of guide dog robots. Video demonstration (best viewed with audio) available at: https://youtu.be/8-pz_8Hqe6s.

