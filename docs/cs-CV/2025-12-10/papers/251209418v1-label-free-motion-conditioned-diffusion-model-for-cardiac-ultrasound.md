---
layout: default
title: Label-free Motion-Conditioned Diffusion Model for Cardiac Ultrasound Synthesis
---

# Label-free Motion-Conditioned Diffusion Model for Cardiac Ultrasound Synthesis

**arXiv**: [2512.09418v1](https://arxiv.org/abs/2512.09418) | [PDF](https://arxiv.org/pdf/2512.09418.pdf)

**作者**: Zhe Li, Hadrien Reynaud, Johanna P Müller, Bernhard Kainz

---

## 💡 一句话要点

**提出无标签运动条件扩散模型，基于自监督运动特征合成心脏超声视频**

**关键词**: `心脏超声合成` `无标签生成` `运动条件扩散模型` `自监督特征学习` `视频生成`

## 📋 核心要点

1. 核心问题：心脏超声标注数据稀缺，阻碍深度学习应用
2. 方法要点：设计运动与外观特征提取器，结合辅助损失增强特征学习
3. 实验或效果：在EchoNet-Dynamic数据集上生成时序连贯、临床真实的视频序列

## 📄 摘要（原文）

> Ultrasound echocardiography is essential for the non-invasive, real-time assessment of cardiac function, but the scarcity of labelled data, driven by privacy restrictions and the complexity of expert annotation, remains a major obstacle for deep learning methods. We propose the Motion Conditioned Diffusion Model (MCDM), a label-free latent diffusion framework that synthesises realistic echocardiography videos conditioned on self-supervised motion features. To extract these features, we design the Motion and Appearance Feature Extractor (MAFE), which disentangles motion and appearance representations from videos. Feature learning is further enhanced by two auxiliary objectives: a re-identification loss guided by pseudo appearance features and an optical flow loss guided by pseudo flow fields. Evaluated on the EchoNet-Dynamic dataset, MCDM achieves competitive video generation performance, producing temporally coherent and clinically realistic sequences without reliance on manual labels. These results demonstrate the potential of self-supervised conditioning for scalable echocardiography synthesis. Our code is available at https://github.com/ZheLi2020/LabelfreeMCDM.

