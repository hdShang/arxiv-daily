---
layout: default
title: A Novel Dual-Stream Framework for dMRI Tractography Streamline Classification with Joint dMRI and fMRI Data
---

# A Novel Dual-Stream Framework for dMRI Tractography Streamline Classification with Joint dMRI and fMRI Data

**arXiv**: [2511.18781v1](https://arxiv.org/abs/2511.18781) | [PDF](https://arxiv.org/pdf/2511.18781.pdf)

**作者**: Haotian Yan, Bocheng Guo, Jianzhong He, Nir A. Sochen, Ofer Pasternak, Lauren J O'Donnell, Fan Zhang

---

## 💡 一句话要点

**提出双流框架联合dMRI和fMRI数据以增强白质束流线分类的功能一致性**

**关键词**: `扩散MRI` `功能MRI` `白质束分类` `双流网络` `流线分析`

## 📋 核心要点

1. 核心问题：现有方法依赖几何特征，无法区分功能不同但路径相似的纤维束
2. 方法要点：设计双流网络，主网络处理全流线轨迹，辅助网络处理fMRI端点信号
3. 实验或效果：在皮质脊髓束分区中，通过消融实验和对比显示性能优越

## 📄 摘要（原文）

> Streamline classification is essential to identify anatomically meaningful white matter tracts from diffusion MRI (dMRI) tractography. However, current streamline classification methods rely primarily on the geometric features of the streamline trajectory, failing to distinguish between functionally distinct fiber tracts with similar pathways. To address this, we introduce a novel dual-stream streamline classification framework that jointly analyzes dMRI and functional MRI (fMRI) data to enhance the functional coherence of tract parcellation. We design a novel network that performs streamline classification using a pretrained backbone model for full streamline trajectories, while augmenting with an auxiliary network that processes fMRI signals from fiber endpoint regions. We demonstrate our method by parcellating the corticospinal tract (CST) into its four somatotopic subdivisions. Experimental results from ablation studies and comparisons with state-of-the-art methods demonstrate our approach's superior performance.

