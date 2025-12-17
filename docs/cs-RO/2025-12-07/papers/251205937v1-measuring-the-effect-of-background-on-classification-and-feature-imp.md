---
layout: default
title: Measuring the Effect of Background on Classification and Feature Importance in Deep Learning for AV Perception
---

# Measuring the Effect of Background on Classification and Feature Importance in Deep Learning for AV Perception

**arXiv**: [2512.05937v1](https://arxiv.org/abs/2512.05937) | [PDF](https://arxiv.org/pdf/2512.05937.pdf)

**作者**: Anne Sielemann, Valentin Barner, Stefan Wolf, Masoud Roschani, Jens Ziehn, Juergen Beyerer

---

## 💡 一句话要点

**提出合成数据集方法以量化背景相关性对自动驾驶感知中深度学习分类与特征重要性的影响**

**关键词**: `可解释AI` `合成数据集` `背景相关性` `特征重要性` `交通标志识别` `深度学习分类`

## 📋 核心要点

1. 核心问题：现有可解释AI方法难以定量测试背景像素对分类结果的影响，导致解释本身缺乏解释性
2. 方法要点：系统生成六个合成数据集，仅改变相机变化和背景相关性，以隔离背景影响
3. 实验或效果：量化背景特征重要性变化，揭示训练域变化如何影响分类性能

## 📄 摘要（原文）

> Common approaches to explainable AI (XAI) for deep learning focus on analyzing the importance of input features on the classification task in a given model: saliency methods like SHAP and GradCAM are used to measure the impact of spatial regions of the input image on the classification result. Combined with ground truth information about the location of the object in the input image (e.g., a binary mask), it is determined whether object pixels had a high impact on the classification result, or whether the classification focused on background pixels. The former is considered to be a sign of a healthy classifier, whereas the latter is assumed to suggest overfitting on spurious correlations. A major challenge, however, is that these intuitive interpretations are difficult to test quantitatively, and hence the output of such explanations lacks an explanation itself. One particular reason is that correlations in real-world data are difficult to avoid, and whether they are spurious or legitimate is debatable. Synthetic data in turn can facilitate to actively enable or disable correlations where desired but often lack a sufficient quantification of realism and stochastic properties. [...] Therefore, we systematically generate six synthetic datasets for the task of traffic sign recognition, which differ only in their degree of camera variation and background correlation [...] to quantify the isolated influence of background correlation, different levels of camera variation, and considered traffic sign shapes on the classification performance, as well as background feature importance. [...] Results include a quantification of when and how much background features gain importance to support the classification task based on changes in the training domain [...].
>   Download: synset.de/datasets/synset-signset-ger/background-effect

