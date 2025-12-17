---
layout: default
title: OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer
---

# OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer

**arXiv**: [2512.08920v1](https://arxiv.org/abs/2512.08920) | [PDF](https://arxiv.org/pdf/2512.08920.pdf)

**作者**: Jessica Yin, Haozhi Qi, Youngsun Wi, Sayantan Kundu, Mike Lambeta, William Yang, Changhao Wang, Tingfan Wu, Jitendra Malik, Tess Hellebrekers

---

## 💡 一句话要点

**提出开源触觉手套OSMO，通过人类演示实现机器人接触丰富任务的技能迁移。**

**关键词**: `触觉感知` `技能迁移` `开源硬件` `机器人操作` `人类演示`

## 📋 核心要点

1. 问题：人类视频演示缺乏接触信号，限制机器人掌握接触丰富的操作任务。
2. 方法：OSMO手套配备12个三轴触觉传感器，兼容手部追踪，最小化视觉和触觉体现差距。
3. 效果：在真实擦拭任务中，仅基于人类演示训练的机器人策略成功率72%，优于纯视觉基线。

## 📄 摘要（原文）

> Human video demonstrations provide abundant training data for learning robot policies, but video alone cannot capture the rich contact signals critical for mastering manipulation. We introduce OSMO, an open-source wearable tactile glove designed for human-to-robot skill transfer. The glove features 12 three-axis tactile sensors across the fingertips and palm and is designed to be compatible with state-of-the-art hand-tracking methods for in-the-wild data collection. We demonstrate that a robot policy trained exclusively on human demonstrations collected with OSMO, without any real robot data, is capable of executing a challenging contact-rich manipulation task. By equipping both the human and the robot with the same glove, OSMO minimizes the visual and tactile embodiment gap, enabling the transfer of continuous shear and normal force feedback while avoiding the need for image inpainting or other vision-based force inference. On a real-world wiping task requiring sustained contact pressure, our tactile-aware policy achieves a 72% success rate, outperforming vision-only baselines by eliminating contact-related failure modes. We release complete hardware designs, firmware, and assembly instructions to support community adoption.

